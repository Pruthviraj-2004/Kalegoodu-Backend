# Generated by Django 4.2.14 on 2024-08-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kalegooduapp", "0005_alter_product_discounted_price_alter_product_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="sale_types",
            field=models.ManyToManyField(
                related_name="products", to="kalegooduapp.saletype"
            ),
        ),
    ]
