# Generated by Django 4.1.3 on 2022-11-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobol', '0003_taskdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.TextField(default='{}')),
            ],
        ),
    ]
