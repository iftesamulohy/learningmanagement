# Generated by Django 4.2.11 on 2024-09-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_alter_specialcta_button_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
