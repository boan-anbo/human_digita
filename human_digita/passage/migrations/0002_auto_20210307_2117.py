# Generated by Django 3.1.7 on 2021-03-07 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passage',
            name='activate_date',
        ),
        migrations.RemoveField(
            model_name='passage',
            name='deactivate_date',
        ),
        migrations.RemoveField(
            model_name='passage',
            name='status',
        ),
    ]
