# Generated by Django 5.0.2 on 2025-02-21 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=300)),
                ('country', models.CharField(default='default', max_length=300)),
                ('city', models.CharField(default='default', max_length=300)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaterBottle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=12, unique=True)),
                ('brand', models.CharField(max_length=300)),
                ('Cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.CharField(max_length=100)),
                ('mouth_size', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('current_quantity', models.IntegerField()),
                ('supplied_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MyInventoryApp.supplier')),
            ],
        ),
    ]
