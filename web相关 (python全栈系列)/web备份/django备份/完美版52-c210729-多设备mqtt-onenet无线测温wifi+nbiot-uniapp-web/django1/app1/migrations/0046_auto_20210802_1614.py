# Generated by Django 2.2.7 on 2021-08-02 16:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0045_auto_20210802_1544'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AddField(
            model_name='info',
            name='data1',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='info',
            name='data1alertstatus',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='info',
            name='data1alerttime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='data1set',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='info',
            name='ledstatus',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='info',
            name='temptime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
