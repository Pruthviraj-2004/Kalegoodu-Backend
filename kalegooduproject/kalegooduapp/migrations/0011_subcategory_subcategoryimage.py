# Generated by Django 4.2.14 on 2025-02-22 05:37

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kalegooduapp', '0010_category_header_category_home_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('subcategory_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('header', models.BooleanField(default=True)),
                ('category_page', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='kalegooduapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoryImage',
            fields=[
                ('subcategory_image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('alt_text', models.CharField(blank=True, max_length=255, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='kalegooduapp.subcategory')),
            ],
        ),
    ]
