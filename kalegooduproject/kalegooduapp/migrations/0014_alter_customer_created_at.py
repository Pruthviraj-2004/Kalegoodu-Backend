# Generated by Django 4.2.14 on 2024-08-27 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kalegooduapp", "0013_order_count"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
