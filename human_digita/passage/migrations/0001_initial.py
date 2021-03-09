# Generated by Django 3.1.7 on 2021-03-09 02:05

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passage',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('before_text', ckeditor.fields.RichTextField(blank=True, max_length=65535)),
                ('text', ckeditor.fields.RichTextField(blank=True, max_length=65535)),
                ('after_text', ckeditor.fields.RichTextField(blank=True, max_length=65535)),
                ('location', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='passage', to='location.location')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
