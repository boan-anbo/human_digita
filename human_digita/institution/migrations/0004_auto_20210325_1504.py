# Generated by Django 3.1.7 on 2021-03-25 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0003_institution_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='start_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='start_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='start_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]