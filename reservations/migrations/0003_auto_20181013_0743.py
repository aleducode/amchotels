# Generated by Django 2.1.2 on 2018-10-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20181012_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='user/pictures'),
        ),
        migrations.AlterField(
            model_name='restrictionhotels',
            name='date_off',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='restrictionhotels',
            name='date_on',
            field=models.DateField(),
        ),
    ]
