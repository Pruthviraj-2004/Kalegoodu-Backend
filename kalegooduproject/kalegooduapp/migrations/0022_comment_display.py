# Generated by Django 4.2.14 on 2024-09-17 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kalegooduapp", "0021_order_order_completed_orderitem_order_completed"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="display",
            field=models.BooleanField(default=False),
        ),
    ]
