# Generated by Django 4.2 on 2023-04-27 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_userprofile_user_userprofile_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='friends',
            field=models.ManyToManyField(to='main_app.userprofile'),
        ),
    ]
