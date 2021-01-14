# Generated by Django 2.1.5 on 2021-01-13 19:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20210113_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 13, 19, 7, 30, 582898, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
