# Generated by Django 3.2.5 on 2022-11-03 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiving', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]