# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20170521_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='parent_product_five',
        ),
        migrations.RemoveField(
            model_name='product',
            name='parent_product_four',
        ),
        migrations.RemoveField(
            model_name='product',
            name='parent_product_one',
        ),
        migrations.RemoveField(
            model_name='product',
            name='parent_product_six',
        ),
        migrations.RemoveField(
            model_name='product',
            name='parent_product_three',
        ),
        migrations.RemoveField(
            model_name='product',
            name='parent_product_two',
        ),
        migrations.AddField(
            model_name='product',
            name='related_products',
            field=models.ManyToManyField(related_name='_product_related_products_+', to='products.Product'),
        ),
    ]