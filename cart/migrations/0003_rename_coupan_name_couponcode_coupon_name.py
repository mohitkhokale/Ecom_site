# Generated by Django 4.0.2 on 2022-02-23 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_couponcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='couponcode',
            old_name='coupan_name',
            new_name='coupon_name',
        ),
    ]