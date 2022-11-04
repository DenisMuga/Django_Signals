from django.db import models
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from datetime import datetime
import json
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=200, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class TaskDate(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)


class History(models.Model):
    history = models.TextField(default='{}')

# def task_handler(sender, instance, **kwargs):
#     print('We are implementing django signals')
#     print(instance.name)
#     print(instance.description)


# pre_save.connect(task_handler, sender=Task)


@receiver(pre_save, sender=Task)
def task_handler(sender, instance, **kwargs):
    print('Writing signals Using receiver')
    print(slugify(instance.name))
    instance.slug = (slugify(instance.name))
    print(slugify(instance.description))

@receiver(post_save, sender=Task)
def task_handler_post(sender, instance, **kwargs):
    TaskDate.objects.create(task=instance, date = datetime.now())

@receiver(pre_delete, sender=Task)
def task_handler_pre_delete(sender, instance, **kwargs):
    data = {'task': instance.task, 'desc': instance.description, 'slug': instance.slug}
    History.objects.create(history=json.dumps(data))


