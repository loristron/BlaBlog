# Generated by Django 2.1.5 on 2021-01-11 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_postcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='hello-world'),
            preserve_default=False,
        ),
    ]
