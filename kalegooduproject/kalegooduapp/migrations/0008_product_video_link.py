# Generated by Django 4.2.14 on 2024-08-15 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kalegooduapp", "0007_comment_rating_alter_product_short_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="video_link",
            field=models.URLField(blank=True, null=True),
        ),
    ]
