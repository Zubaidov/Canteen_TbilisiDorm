# Generated by Django 5.0 on 2023-12-21 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_menu_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='category',
            new_name='categories',
        ),
    ]
