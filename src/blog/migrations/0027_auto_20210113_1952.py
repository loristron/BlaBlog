# Generated by Django 2.1.5 on 2021-01-13 22:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20210113_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 13, 22, 52, 48, 842440, tzinfo=utc), null=True),
        ),
    ]
