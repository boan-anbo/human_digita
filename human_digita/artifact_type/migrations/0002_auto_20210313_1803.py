# Generated by Django 3.1.7 on 2021-03-13 17:03

import uuid

import ckeditor.fields
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifact_type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtifactType',
            fields=[
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('name_cn', models.CharField(blank=True, max_length=255)),
                ('note', ckeditor.fields.RichTextField(blank=True, default='', max_length=2000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Artifact',
        ),
    ]
