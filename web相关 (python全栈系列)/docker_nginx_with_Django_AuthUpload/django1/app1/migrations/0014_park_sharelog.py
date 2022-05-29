# Generated by Django 2.2.7 on 2021-03-01 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_auto_20210124_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('numid', models.IntegerField(default=-1)),
                ('carstatus', models.BooleanField(default=True)),
                ('sharestatus', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sharelog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addtime', models.DateTimeField(auto_now_add=True)),
                ('outtime', models.DateTimeField(null=True)),
                ('client', models.CharField(default='', max_length=30)),
                ('numid', models.IntegerField(default=-1)),
            ],
        ),
    ]
