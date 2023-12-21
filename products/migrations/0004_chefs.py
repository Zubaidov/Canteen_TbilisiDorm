# Generated by Django 5.0 on 2023-12-21 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_menu_author_alter_menu_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('HC', 'HEAD CHEF'), ('AS', 'ASSISTENT')], default='AS', max_length=2)),
                ('insta', models.CharField(max_length=255)),
                ('teleg', models.CharField(max_length=255)),
            ],
        ),
    ]