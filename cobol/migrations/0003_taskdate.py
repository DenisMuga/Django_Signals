# Generated by Django 4.1.3 on 2022-11-04 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cobol', '0002_task_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobol.task')),
            ],
        ),
    ]
