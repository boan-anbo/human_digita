# Generated by Django 3.1.7 on 2021-03-15 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='importance',
            field=models.IntegerField(blank=True, choices=[(0, 'Unknown'), (1, 'Lowest'), (2, 'Low'), (3, 'Medium'), (4, 'High'), (5, 'Highest')], default=0),
        ),
    ]
