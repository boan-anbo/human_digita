# Generated by Django 3.1.7 on 2021-03-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_document_author_string'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='author_string',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]