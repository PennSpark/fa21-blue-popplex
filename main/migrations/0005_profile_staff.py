# Generated by Django 2.2.24 on 2021-12-08 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_tweet'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]