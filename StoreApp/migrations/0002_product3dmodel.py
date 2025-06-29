# Generated by Django 5.1.2 on 2025-06-14 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product3DModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_file', models.FileField(upload_to='products/3d_models/')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models_3d', to='StoreApp.product')),
            ],
        ),
    ]
