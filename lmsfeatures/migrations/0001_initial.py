# Generated by Django 4.2.11 on 2024-08-29 13:21

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globalapp', '0014_basebeneficariesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseAudience',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('title', models.CharField(max_length=200)),
            ],
            bases=('globalapp.common',),
        ),
        migrations.CreateModel(
            name='CourseContents',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('title', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('content_type', models.CharField(choices=[('video', 'Video'), ('quiz', 'Quiz')], default='video', max_length=10)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('source', models.URLField()),
            ],
            bases=('globalapp.common',),
        ),
        migrations.CreateModel(
            name='CourseFaqs',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('questions', models.CharField(max_length=200)),
                ('answear', ckeditor.fields.RichTextField()),
            ],
            bases=('globalapp.common',),
        ),
        migrations.CreateModel(
            name='CourseLevel',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('level_name', models.CharField(max_length=200)),
            ],
            bases=('globalapp.common',),
        ),
        migrations.CreateModel(
            name='CourseModules',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('title', models.CharField(max_length=200)),
                ('contents', models.ManyToManyField(to='lmsfeatures.coursecontents')),
            ],
            bases=('globalapp.common',),
        ),
        migrations.CreateModel(
            name='CoursePrerequisit',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('title', models.CharField(max_length=200)),
                ('icon', models.ImageField(upload_to='')),
            ],
            bases=('globalapp.common',),
        ),
        migrations.CreateModel(
            name='CourseTopics',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('title', models.CharField(max_length=200)),
            ],
            bases=('globalapp.common',),
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('type_name', models.CharField(max_length=200)),
            ],
            bases=('globalapp.common',),
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('title', models.CharField(max_length=200)),
                ('student_amount', models.IntegerField(blank=True, null=True)),
                ('course_thumbnail', models.ImageField(upload_to='')),
                ('live_projects', models.IntegerField(blank=True, null=True)),
                ('intro_title', models.CharField(max_length=200)),
                ('intro_video_url', models.URLField()),
                ('total_students', models.IntegerField(blank=True, null=True)),
                ('remaining_students', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('offer_price', models.FloatField()),
                ('milestone_count', models.IntegerField()),
                ('module_count', models.IntegerField()),
                ('video_count', models.IntegerField()),
                ('quiz_count', models.IntegerField()),
                ('course_audiences', models.ManyToManyField(to='lmsfeatures.courseaudience')),
                ('course_faqs', models.ManyToManyField(to='lmsfeatures.coursefaqs')),
                ('course_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsfeatures.courselevel')),
                ('course_topics', models.ManyToManyField(to='lmsfeatures.coursetopics')),
                ('course_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsfeatures.coursetype')),
                ('milestones', models.ManyToManyField(to='lmsfeatures.coursemodules')),
                ('prerequisites', models.ManyToManyField(to='lmsfeatures.courseprerequisit')),
            ],
            bases=('globalapp.common',),
        ),
        migrations.CreateModel(
            name='CourseMilestones',
            fields=[
                ('common_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp.common')),
                ('title', models.CharField(max_length=200)),
                ('modules', models.ManyToManyField(to='lmsfeatures.coursemodules')),
            ],
            bases=('globalapp.common',),
        ),
    ]
