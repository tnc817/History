# Generated by Django 2.2.7 on 2021-01-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20210124_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='outtime',
            field=models.DateTimeField(null=True),
        ),
    ]
