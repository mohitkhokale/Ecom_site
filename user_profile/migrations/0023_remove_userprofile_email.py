# Generated by Django 4.0.2 on 2022-02-22 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0022_userprofile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
