# Generated by Django 3.2.6 on 2022-05-30 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0014_courseschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter_course',
            name='user',
        ),
        migrations.RemoveField(
            model_name='screan_course',
            name='user',
        ),
        migrations.RemoveField(
            model_name='topic_course',
            name='user',
        ),
        migrations.AddField(
            model_name='chapter_course',
            name='chapterid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='screan_course',
            name='screanid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='topic_course',
            name='tpicid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
