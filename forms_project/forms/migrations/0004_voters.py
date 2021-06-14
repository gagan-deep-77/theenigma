# Generated by Django 3.2 on 2021-05-29 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_options_room_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('option', models.CharField(max_length=1000)),
                ('question', models.CharField(max_length=1000)),
                ('room_name', models.CharField(default='', max_length=500)),
            ],
        ),
    ]