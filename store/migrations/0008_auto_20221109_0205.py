# Generated by Django 3.1 on 2022-11-09 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20221109_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variationproduct',
            name='variation_product_color',
            field=models.ManyToManyField(blank=True, to='store.VariationProductColor'),
        ),
        migrations.AlterField(
            model_name='variationproduct',
            name='variation_product_plus',
            field=models.ManyToManyField(blank=True, to='store.VariationProductPlus'),
        ),
        migrations.AlterField(
            model_name='variationproduct',
            name='variation_product_size',
            field=models.ManyToManyField(blank=True, to='store.VariationProductSize'),
        ),
    ]
