# Generated by Django 5.0.1 on 2024-01-27 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eval', '0007_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='operador',
            field=models.IntegerField(default=2, null=True),
        ),
    ]
