# Generated by Django 3.2a1 on 2021-01-24 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jedzenieonline', '0002_klienci_wlasciciel'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkty',
            name='wlasciciel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='produkty', to='auth.user'),
            preserve_default=False,
        ),
    ]
