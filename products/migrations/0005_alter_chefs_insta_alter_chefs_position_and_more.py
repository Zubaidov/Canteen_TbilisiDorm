# Generated by Django 5.0 on 2023-12-21 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_chefs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chefs',
            name='insta',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='position',
            field=models.CharField(choices=[('HEAD CHEF', 'HEAD CHEF'), ('ASSISTENT', 'ASSISTENT')], default='ASSISTENT', max_length=50),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='teleg',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
