# Generated by Django 2.1.4 on 2019-01-06 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccount', '0011_auto_20190106_2132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='antrag',
            options={'permissions': (('can_add_Antrag', 'Kann einen Antrag erstellen'), ('can_see_Antrag', 'Kann einen Antrag sehen'))},
        ),
    ]
