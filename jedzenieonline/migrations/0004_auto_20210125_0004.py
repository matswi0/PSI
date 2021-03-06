# Generated by Django 3.1.5 on 2021-01-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzenieonline', '0003_produkty_wlasciciel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dostawcy',
            name='status_dostawcy_id',
        ),
        migrations.RemoveField(
            model_name='dostawcy',
            name='zarobki_id',
        ),
        migrations.AddField(
            model_name='dostawcy',
            name='dostepnosc_dostawcy',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dostawcy',
            name='numer_umowy',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dostawcy',
            name='przepracowane_godziny',
            field=models.IntegerField(default=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dostawcy',
            name='stawka_godzinowa',
            field=models.IntegerField(default=17),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='StatusDostawcy',
        ),
        migrations.DeleteModel(
            name='Zarobki',
        ),
    ]
