# Generated by Django 4.2.14 on 2024-09-13 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kalegooduapp", "0018_workshop_workshopvideo_workshopimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="workshop",
            name="name",
            field=models.CharField(default="a", max_length=255),
            preserve_default=False,
        ),
    ]
