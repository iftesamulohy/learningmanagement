# Generated by Django 4.2.11 on 2024-07-06 09:43

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globalapp', '0013_delete_basebeneficariesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('name', models.TextField()),
                ('description', ckeditor.fields.RichTextField()),
                ('content', ckeditor.fields.RichTextField()),
                ('pub_status', models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLISHED', 'Published')], default='DRAFT', max_length=10)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            bases=('globalapp.common',),
        ),
    ]
