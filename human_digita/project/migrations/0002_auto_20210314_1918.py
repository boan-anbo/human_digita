# Generated by Django 3.1.7 on 2021-03-14 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='name',
        ),
    ]
