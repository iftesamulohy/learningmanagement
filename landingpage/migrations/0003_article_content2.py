# Generated by Django 4.2.11 on 2025-01-20 15:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0002_alter_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content2',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
