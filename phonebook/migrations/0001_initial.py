# Generated by Django 5.0.3 on 2024-04-21 05:52

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('name', models.CharField(max_length=100)),
                ('relation', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
            bases=('globalapp.common',),
        ),
    ]
