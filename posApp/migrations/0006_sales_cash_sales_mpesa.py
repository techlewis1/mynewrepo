# Generated by Django 5.0.4 on 2024-05-31 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0005_products_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='cash',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='mpesa',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]