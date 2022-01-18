# Generated by Django 3.1 on 2022-01-18 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('file', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest_problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('order', models.IntegerField()),
                ('contest_id', models.ForeignKey(db_column='contest_id', on_delete=django.db.models.deletion.CASCADE, to='contest.contest')),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('data_description', models.TextField()),
                ('public', models.BooleanField(default=True)),
                ('contests', models.ManyToManyField(through='problem.Contest_problem', to='contest.Contest')),
                ('created_user', models.ForeignKey(db_column='created_user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('data', models.ForeignKey(db_column='data', on_delete=django.db.models.deletion.CASCADE, to='file.file')),
            ],
            options={
                'db_table': 'problem',
            },
        ),
        migrations.AddField(
            model_name='contest_problem',
            name='problem_id',
            field=models.ForeignKey(db_column='problem_id', on_delete=django.db.models.deletion.CASCADE, to='problem.problem'),
        ),
    ]