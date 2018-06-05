# Generated by Django 2.0.5 on 2018-06-04 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_productimage_is_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=16, null=True)),
            ],
            options={
                'verbose_name': 'Категория товаров',
                'verbose_name_plural': 'Категории товаров',
            },
        ),
    ]