# Generated by Django 3.1.7 on 2021-03-14 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
        ('act', '0003_act_act_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='act',
            name='timelines',
            field=models.ManyToManyField(blank=True, related_name='acts', to='timeline.Timeline'),
        ),
    ]
