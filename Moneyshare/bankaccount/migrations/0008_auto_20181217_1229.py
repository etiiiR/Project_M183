# Generated by Django 2.1.4 on 2018-12-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccount', '0007_auto_20181217_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccoount',
            name='Money',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='transaktion',
            name='Value',
            field=models.PositiveIntegerField(default=1),
        ),
    ]