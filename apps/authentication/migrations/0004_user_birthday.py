# Generated by Django 3.2.6 on 2022-03-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20220319_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]