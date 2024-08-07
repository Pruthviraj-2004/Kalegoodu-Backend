# Generated by Django 4.2.14 on 2024-08-07 18:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kalegooduapp", "0006_alter_product_sale_types"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="rating",
            field=models.IntegerField(
                blank=True,
                default=3,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="short_description",
            field=models.TextField(blank=True, null=True),
        ),
    ]