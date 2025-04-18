# Generated by Django 4.2.11 on 2024-07-06 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globalapp', '0013_delete_basebeneficariesmodel'),
        ('cms', '0004_blog_slug_faq_slug_page_slug_testimonial_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerItem',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('image', models.ImageField(upload_to='banner_images/')),
                ('link', models.URLField(blank=True, null=True)),
                ('order', models.PositiveIntegerField()),
            ],
            bases=('globalapp.common',),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('items', models.ManyToManyField(related_name='banners', to='cms.banneritem')),
            ],
            bases=('globalapp.common',),
        ),
    ]
