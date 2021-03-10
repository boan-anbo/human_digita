# Generated by Django 3.1.7 on 2021-03-09 02:05

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('document', '0001_initial'),
        ('keyterm', '0001_initial'),
        ('comment', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('marked_text', ckeditor.fields.RichTextField(blank=True, max_length=65535)),
                ('modified_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('annotation_type', models.CharField(blank=True, max_length=255)),
                ('page_index', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('comments', models.ManyToManyField(blank=True, related_name='annotations', to='comment.Comment')),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='annotations', to='document.document')),
                ('keyterms', models.ManyToManyField(blank=True, related_name='annotations', to='keyterm.Keyterm')),
                ('projects', models.ManyToManyField(blank=True, related_name='annotations', to='project.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]