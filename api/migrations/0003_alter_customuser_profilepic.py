# Generated by Django 4.0.6 on 2022-07-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_customuser_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profilePic',
            field=models.ImageField(blank=True, default='img/default-avatar.jpg', null=True, upload_to='img/'),
        ),
    ]