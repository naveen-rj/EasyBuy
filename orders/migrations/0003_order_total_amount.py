# Generated by Django 5.0.2 on 2024-03-16 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderitem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.FloatField(null=True),
        ),
    ]
