# Generated by Django 5.0 on 2023-12-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_rename_aboutcanteen_pageabout_rename_menu_products_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chefs',
            name='insta',
            field=models.CharField(default='https://www.instagram.com/', editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='teleg',
            field=models.CharField(default='https://www.instagram.com/', max_length=255),
        ),
    ]
