# Generated by Django 2.1.2 on 2019-05-29 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_auto_20181013_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='total',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='total_amc',
            field=models.IntegerField(),
        ),
    ]