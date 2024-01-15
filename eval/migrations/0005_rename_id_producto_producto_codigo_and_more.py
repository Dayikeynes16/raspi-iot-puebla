# Generated by Django 4.2.7 on 2024-01-12 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eval', '0004_productoventa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='id_producto',
            new_name='codigo',
        ),
        migrations.AlterField(
            model_name='productoventa',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
