# Generated by Django 4.0.2 on 2022-03-03 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 3, 19, 6, 22, 83147)),
        ),
    ]
