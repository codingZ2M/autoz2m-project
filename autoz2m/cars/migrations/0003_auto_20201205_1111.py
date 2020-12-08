# Generated by Django 3.1.3 on 2020-12-05 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20201205_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(max_length=50),
        ),
    ]