# Generated by Django 3.1.7 on 2021-03-09 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_remove_document_modified_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='author_string',
            field=models.CharField(blank=True, max_length=512),
        ),
    ]