# Generated by Django 3.2 on 2022-02-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
