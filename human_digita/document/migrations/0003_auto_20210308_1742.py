# Generated by Django 3.1.7 on 2021-03-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_auto_20210307_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.CharField(choices=[('DOCUMENT', 'Document'), ('WEB', 'Web')], default='DOCUMENT', max_length=200),
        ),
    ]
