# Generated by Django 4.0.2 on 2022-02-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0017_alter_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='pending@gm.com', help_text='Email', max_length=254),
        ),
    ]
