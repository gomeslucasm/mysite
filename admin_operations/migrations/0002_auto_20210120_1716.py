# Generated by Django 3.1.5 on 2021-01-20 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_operations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='operation_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operation_types', to='admin_operations.operationtype'),
        ),
    ]
