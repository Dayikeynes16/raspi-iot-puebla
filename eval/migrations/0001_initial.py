# Generated by Django 4.2.7 on 2023-12-27 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]