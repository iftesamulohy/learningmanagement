# Generated by Django 4.2.11 on 2024-09-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsfeatures', '0010_paymentmethods_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirm', 'Confirm'), ('due', 'Due')], default='pending', max_length=15),
        ),
    ]
