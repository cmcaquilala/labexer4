# Generated by Django 3.1.7 on 2021-05-28 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_crud', '0004_auto_20210528_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='languages',
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
