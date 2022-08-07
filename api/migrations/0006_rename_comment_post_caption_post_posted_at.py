# Generated by Django 4.0.6 on 2022-08-06 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='comment',
            new_name='caption',
        ),
        migrations.AddField(
            model_name='post',
            name='posted_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]