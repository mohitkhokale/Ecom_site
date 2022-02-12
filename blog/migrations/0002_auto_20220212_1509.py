# Generated by Django 3.2 on 2022-02-12 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
