# Generated by Django 3.1.5 on 2021-01-17 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_animals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationinfo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='animalphoto',
            name='animal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal_photo', to='admin_animals.animal'),
        ),
        migrations.AddField(
            model_name='animal',
            name='responsible_volunteer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='volunteer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='animal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
