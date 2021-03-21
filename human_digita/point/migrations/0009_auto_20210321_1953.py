# Generated by Django 3.1.7 on 2021-03-21 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('point', '0008_auto_20210321_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='children',
        ),
        migrations.AddField(
            model_name='point',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='point.point'),
        ),
    ]
