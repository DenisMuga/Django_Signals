from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# def task_handler(sender, instance, **kwargs):
#     print('We are implementing django signals')
#     print(instance.name)
#     print(instance.description)


# pre_save.connect(task_handler, sender=Task)



