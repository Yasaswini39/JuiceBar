# Generated by Django 5.1.3 on 2025-01-29 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='number',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
