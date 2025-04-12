# Generated by Django 4.2.11 on 2024-09-01 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globalapp', '0014_basebeneficariesmodel'),
        ('cms', '0006_button_banneritem_descriptions_banneritem_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CounterItem',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('title', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
            ],
            bases=('globalapp.common',),
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter_item', models.ManyToManyField(to='cms.counteritem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
