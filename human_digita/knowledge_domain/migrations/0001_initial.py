# Generated by Django 3.1.7 on 2021-03-15 13:40

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0003_auto_20210315_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeDomain',
            fields=[
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('note', ckeditor.fields.RichTextField(blank=True, default='', max_length=65535)),
                ('projects', models.ManyToManyField(blank=True, related_name='knowledgeDomains', to='project.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]