# Generated by Django 3.1 on 2022-01-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='privilege',
            field=models.IntegerField(null=True),
        ),
    ]