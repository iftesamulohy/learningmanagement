# Generated by Django 4.2.11 on 2025-02-06 14:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0010_purchase_payment_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('css_code', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('body_content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('js_code', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
