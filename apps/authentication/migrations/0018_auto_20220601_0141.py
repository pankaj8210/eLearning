# Generated by Django 3.2.6 on 2022-05-31 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0017_auto_20220531_0617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='courselogo',
        ),
        migrations.AddField(
            model_name='courses',
            name='screan',
            field=models.ImageField(blank=True, null=True, upload_to='courselogos'),
        ),
    ]
