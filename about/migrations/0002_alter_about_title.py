# Generated by Django 4.2.8 on 2023-12-29 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]