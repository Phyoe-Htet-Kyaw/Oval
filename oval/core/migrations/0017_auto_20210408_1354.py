# Generated by Django 3.1.7 on 2021-04-08 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20210407_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
