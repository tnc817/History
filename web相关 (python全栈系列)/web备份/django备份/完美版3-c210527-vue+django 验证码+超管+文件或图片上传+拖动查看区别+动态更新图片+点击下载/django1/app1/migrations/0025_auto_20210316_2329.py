# Generated by Django 2.2.7 on 2021-03-16 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_status_alerttime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='alertmail',
        ),
        migrations.RemoveField(
            model_name='status',
            name='alerttime',
        ),
        migrations.RemoveField(
            model_name='status',
            name='deltamin',
        ),
        migrations.RemoveField(
            model_name='status',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='status',
            name='leavetime',
        ),
        migrations.RemoveField(
            model_name='status',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='status',
            name='orilat',
        ),
        migrations.RemoveField(
            model_name='status',
            name='orilon',
        ),
        migrations.AddField(
            model_name='status',
            name='hum',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='status',
            name='humset',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='status',
            name='manualstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='status',
            name='period',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='status',
            name='setstatus',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='status',
            name='settime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='status',
            name='temp',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='status',
            name='tempset',
            field=models.FloatField(default=0.0),
        ),
    ]
