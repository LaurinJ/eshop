# Generated by Django 3.1.2 on 2020-10-29 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20201028_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
