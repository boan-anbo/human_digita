# Generated by Django 3.1.7 on 2021-03-11 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passage', '0003_passage_page_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='passage',
            name='language',
            field=models.CharField(choices=[('UNKNOWN', 'Unknown'), ('ENGLISH', 'English'), ('CHINESE', 'Chinese'), ('OTHER', 'Other')], default='UNKNOWN', max_length=120),
        ),
    ]
