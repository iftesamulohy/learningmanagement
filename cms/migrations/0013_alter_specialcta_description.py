# Generated by Django 4.2.11 on 2024-09-01 10:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_alter_specialcta_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialcta',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, default='none', null=True),
        ),
    ]
