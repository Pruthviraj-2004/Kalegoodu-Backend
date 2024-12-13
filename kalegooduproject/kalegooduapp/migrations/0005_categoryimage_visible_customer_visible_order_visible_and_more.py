# Generated by Django 4.2.14 on 2024-12-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kalegooduapp", "0004_saletype_visible"),
    ]

    operations = [
        migrations.AddField(
            model_name="categoryimage",
            name="visible",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="visible",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="order", name="visible", field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="visible",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="pagecontent",
            name="visible",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="pageimage",
            name="visible",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="productimage",
            name="visible",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="workshopimage",
            name="visible",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="workshopvideo",
            name="visible",
            field=models.BooleanField(default=True),
        ),
    ]