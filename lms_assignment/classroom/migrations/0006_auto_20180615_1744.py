# Generated by Django 2.0.1 on 2018-06-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_quiz_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(max_length=12, null=True),
        ),
    ]
