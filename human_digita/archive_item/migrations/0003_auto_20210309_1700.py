# Generated by Django 3.1.7 on 2021-03-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive_item', '0002_auto_20210309_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archiveitem',
            name='title',
            field=models.CharField(max_length=2000),
        ),
    ]