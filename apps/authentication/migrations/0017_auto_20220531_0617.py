# Generated by Django 3.2.6 on 2022-05-31 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0016_auto_20220530_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='coursemodule',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='lastupdateon',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='subjectexp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='totalexp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
