# Generated by Django 2.1.2 on 2018-12-11 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_intro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='intro',
        ),
    ]
