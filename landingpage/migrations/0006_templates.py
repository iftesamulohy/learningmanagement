# Generated by Django 4.2.11 on 2025-01-22 02:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0005_alter_purchase_payment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_code', ckeditor.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
