# Generated by Django 4.2.11 on 2025-01-23 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0007_bkashsettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='BkashConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_key', models.CharField(max_length=100)),
                ('app_secret', models.CharField(max_length=100)),
                ('sandbox', models.BooleanField(default=True)),
            ],
        ),
    ]
