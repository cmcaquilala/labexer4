# Generated by Django 3.1.7 on 2021-05-28 00:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_crud', '0003_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=25), size=None),
        ),
    ]
