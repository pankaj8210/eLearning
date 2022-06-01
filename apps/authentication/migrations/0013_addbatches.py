# Generated by Django 3.2.6 on 2022-05-28 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_auto_20220525_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addbatches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.CharField(blank=True, max_length=255, null=True)),
                ('updatedby', models.CharField(blank=True, max_length=255, null=True)),
                ('lastupdateon', models.CharField(blank=True, max_length=255, null=True)),
                ('starttime', models.CharField(blank=True, max_length=255, null=True)),
                ('enddatetime', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]