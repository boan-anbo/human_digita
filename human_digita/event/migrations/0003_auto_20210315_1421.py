# Generated by Django 3.1.7 on 2021-03-15 13:21

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20210314_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_datetime_local_timezone',
            field=timezone_field.fields.TimeZoneField(default='UTC'),
        ),
    ]