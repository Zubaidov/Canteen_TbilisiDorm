# Generated by Django 5.0 on 2023-12-21 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_category_menu_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='categories',
        ),
    ]
