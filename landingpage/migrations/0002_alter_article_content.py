# Generated by Django 4.2.11 on 2025-01-20 12:32

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
