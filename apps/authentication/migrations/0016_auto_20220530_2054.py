# Generated by Django 3.2.6 on 2022-05-30 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_auto_20220530_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='aboutme',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
