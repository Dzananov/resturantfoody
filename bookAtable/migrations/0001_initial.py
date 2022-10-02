# Generated by Django 3.2.15 on 2022-10-02 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('number_of_persones', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
