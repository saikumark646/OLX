# Generated by Django 4.0.6 on 2022-07-18 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_category_image_alter_prdouctimages_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category/'),
        ),
        migrations.AlterField(
            model_name='prdouctimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]