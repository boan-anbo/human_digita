# Generated by Django 3.1.7 on 2021-03-18 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0004_remove_picture_annotations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='image_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='picture',
            old_name='image_source',
            new_name='source',
        ),
    ]