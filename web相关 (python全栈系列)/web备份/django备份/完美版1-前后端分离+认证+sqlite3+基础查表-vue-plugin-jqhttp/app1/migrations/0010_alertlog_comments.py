# Generated by Django 2.2.7 on 2021-01-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alertlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertlog',
            name='comments',
            field=models.CharField(default='', max_length=30),
        ),
    ]
