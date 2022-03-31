# Generated by Django 3.1 on 2022-03-29 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20220329_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': '중복된 email 입니다.'}, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': '중복된 ID 입니다.'}, max_length=20, unique=True),
        ),
    ]