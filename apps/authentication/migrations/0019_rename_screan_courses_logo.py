# Generated by Django 3.2.6 on 2022-05-31 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0018_auto_20220601_0141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='screan',
            new_name='logo',
        ),
    ]
