# Generated by Django 3.0 on 2021-06-16 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HallBooking', '0002_auto_20210612_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardno', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('expmonth', models.IntegerField(choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')])),
                ('expyear', models.IntegerField(choices=[('1', '2021'), ('2', '2022'), ('3', '2023'), ('4', '2024'), ('5', '2025'), ('6', '2026'), ('7', '2017'), ('8', '2028')])),
                ('amount', models.IntegerField()),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
