# Generated by Django 3.1.7 on 2021-03-13 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0008_auto_20210313_1454'),
        ('artifact_type', '0002_auto_20210313_1803'),
        ('artifact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='annotations',
            field=models.ManyToManyField(blank=True, related_name='annotations', to='annotation.Annotation'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='artifact_types',
            field=models.ManyToManyField(blank=True, related_name='artifacts', to='artifact_type.ArtifactType'),
        ),
    ]