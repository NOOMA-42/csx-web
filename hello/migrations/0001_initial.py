# Generated by Django 2.1.1 on 2018-10-05 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=18, unique=True)),
                ('password', models.CharField(max_length=18, unique=True)),
            ],
        ),
    ]
