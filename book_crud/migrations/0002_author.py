# Generated by Django 3.1.7 on 2021-05-27 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
