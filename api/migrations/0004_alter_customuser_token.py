# Generated by Django 4.0.6 on 2022-07-23 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_customuser_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='token',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
