# Generated by Django 2.0.5 on 2018-06-04 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_auto_20180604_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price_w_discount',
        ),
    ]
