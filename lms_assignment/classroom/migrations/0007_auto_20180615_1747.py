# Generated by Django 2.0.1 on 2018-06-15 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_auto_20180615_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 15, 17, 47, 23, 114675), max_length=12, null=True),
        ),
    ]
