# Generated by Django 4.2.11 on 2024-10-09 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_bannerlms'),
    ]

    operations = [
        migrations.AddField(
            model_name='banneritem',
            name='mobile_image',
            field=models.ImageField(blank=True, null=True, upload_to='banner_images/'),
        ),
    ]
