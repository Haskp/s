# Generated by Django 5.1.2 on 2024-12-05 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compile', '0004_task_date_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default='aafaf', max_length=200),
        ),
    ]
