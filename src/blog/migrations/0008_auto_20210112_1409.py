# Generated by Django 2.1.5 on 2021-01-12 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210112_1357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-updated_stamp', '-time_stamp']},
        ),
    ]
