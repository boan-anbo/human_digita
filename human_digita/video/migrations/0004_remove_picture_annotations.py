# Generated by Django 3.1.7 on 2021-03-18 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20210318_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='annotations',
        ),
    ]
