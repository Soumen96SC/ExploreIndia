# Generated by Django 3.0.2 on 2020-05-09 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0005_auto_20200509_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionhistory',
            name='check_in',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactionhistory',
            name='check_out',
            field=models.DateField(blank=True, null=True),
        ),
    ]
