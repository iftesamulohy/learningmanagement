# Generated by Django 4.2.11 on 2024-05-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalapp', '0009_rename_password_emailconfigure_email_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconfigure',
            name='email_password',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
