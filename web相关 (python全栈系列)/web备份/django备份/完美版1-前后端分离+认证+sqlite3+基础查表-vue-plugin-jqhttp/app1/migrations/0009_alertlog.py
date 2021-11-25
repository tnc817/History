# Generated by Django 2.2.7 on 2021-01-24 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20210124_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(default='', max_length=30)),
                ('type', models.IntegerField(default=0)),
                ('addtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
