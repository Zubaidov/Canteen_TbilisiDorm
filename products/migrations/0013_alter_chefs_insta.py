# Generated by Django 5.0 on 2023-12-22 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_chefs_insta_alter_chefs_teleg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chefs',
            name='insta',
            field=models.CharField(default='https://www.instagram.com/', max_length=255),
        ),
    ]
