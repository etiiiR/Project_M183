# Generated by Django 2.1.3 on 2018-11-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccoount',
            name='Money',
            field=models.IntegerField(default=1),
        ),
    ]
