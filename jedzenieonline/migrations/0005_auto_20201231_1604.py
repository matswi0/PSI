# Generated by Django 3.1.3 on 2020-12-31 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jedzenieonline', '0004_auto_20201231_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daneplatnosci',
            old_name='id_klienta',
            new_name='id_klient',
        ),
    ]
