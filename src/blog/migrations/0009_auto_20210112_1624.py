# Generated by Django 2.1.5 on 2021-01-12 19:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210112_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 12, 19, 24, 45, 856651, tzinfo=utc), null=True),
        ),
    ]
