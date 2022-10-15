# Generated by Django 3.2.15 on 2022-10-15 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('guests', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=2)),
                ('time', models.IntegerField(choices=[(1, '16-17'), (2, '17-18'), (3, '18-19'), (4, '19-20')], default=2)),
                ('date', models.DateField()),
                ('costumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='costumer_reservation', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date', 'time'),
                'unique_together': {('guests', 'time', 'date')},
            },
        ),
    ]
