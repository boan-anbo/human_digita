# Generated by Django 3.1.7 on 2021-03-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('debatable', '0001_initial'),
        ('opinion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='debatable',
            name='acknowledges',
            field=models.ManyToManyField(blank=True, related_name='acknolwedge_debatables', to='opinion.Opinion'),
        ),
        migrations.AddField(
            model_name='debatable',
            name='againsts',
            field=models.ManyToManyField(blank=True, related_name='against_debatables', to='opinion.Opinion'),
        ),
        migrations.AddField(
            model_name='debatable',
            name='denials',
            field=models.ManyToManyField(blank=True, related_name='deny_debatables', to='opinion.Opinion'),
        ),
        migrations.AddField(
            model_name='debatable',
            name='neutrals',
            field=models.ManyToManyField(blank=True, related_name='complicate_debatables', to='opinion.Opinion'),
        ),
        migrations.AddField(
            model_name='debatable',
            name='supports',
            field=models.ManyToManyField(blank=True, related_name='support_debatables', to='opinion.Opinion'),
        ),
    ]