# Generated by Django 4.0.2 on 2022-02-22 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0021_remove_userprofile_email_userprofile_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=1, help_text='Email', max_length=254),
            preserve_default=False,
        ),
    ]
