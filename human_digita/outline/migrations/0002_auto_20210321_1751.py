# Generated by Django 3.1.7 on 2021-03-21 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point', '0005_auto_20210321_0352'),
        ('outline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outline',
            name='points',
            field=models.ManyToManyField(blank=True, related_name='outlines', to='point.Point'),
        ),
    ]
