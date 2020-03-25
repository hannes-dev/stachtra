# Generated by Django 3.0.3 on 2020-03-25 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('steamid', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('avatar', models.CharField(max_length=50)),
                ('vanity_url', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('appid', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=40)),
                ('logo', models.CharField(max_length=40)),
                ('users', models.ManyToManyField(to='sta.User')),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('display_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=60)),
                ('hidden', models.BooleanField()),
                ('icon', models.CharField(max_length=50)),
                ('gray_icon', models.CharField(max_length=50)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sta.App')),
                ('users', models.ManyToManyField(to='sta.User')),
            ],
            options={
                'unique_together': {('name', 'app')},
            },
        ),
    ]
