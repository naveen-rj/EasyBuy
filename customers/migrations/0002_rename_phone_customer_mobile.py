# Generated by Django 5.0.2 on 2024-03-11 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='phone',
            new_name='mobile',
        ),
    ]