# Generated by Django 4.2.11 on 2024-09-04 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('globalapp', '0014_basebeneficariesmodel'),
        ('lmsfeatures', '0003_alter_courses_milestones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('payment_type', models.CharField(choices=[('full', 'Full'), ('installment', 'Installment')], default='full', max_length=15)),
                ('amount', models.FloatField()),
                ('number', models.CharField(max_length=25)),
                ('transaction_id', models.CharField(blank=True, max_length=25, null=True)),
                ('course_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lmsfeatures.courses')),
                ('installation_status', models.ManyToManyField(blank=True, to='lmsfeatures.installationstatus')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('globalapp.common',),
        ),
        migrations.CreateModel(
            name='EnrollCourse',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('payment_type', models.CharField(choices=[('full', 'Full'), ('installment', 'Installment')], default='full', max_length=15)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('course_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lmsfeatures.courses')),
                ('installation_status', models.ManyToManyField(blank=True, to='lmsfeatures.installationstatus')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('globalapp.common',),
        ),
    ]
