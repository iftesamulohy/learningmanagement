# Generated by Django 4.2.11 on 2025-03-12 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0012_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
