# Generated by Django 3.1.7 on 2021-03-18 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive_item', '0005_auto_20210318_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='archiveitem',
            name='file_url',
            field=models.CharField(blank=True, max_length=3000),
        ),
    ]
