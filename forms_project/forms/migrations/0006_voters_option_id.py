# Generated by Django 3.2 on 2021-06-13 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_options_voted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='voters',
            name='option_id',
            field=models.IntegerField(default=0),
        ),
    ]
