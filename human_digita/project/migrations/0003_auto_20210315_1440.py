# Generated by Django 3.1.7 on 2021-03-15 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20210314_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='description',
            new_name='note',
        ),
    ]
