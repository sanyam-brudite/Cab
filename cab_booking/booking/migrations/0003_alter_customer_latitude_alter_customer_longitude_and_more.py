# Generated by Django 5.0.6 on 2024-05-09 11:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0002_rename_user_customer_username_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="latitude",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="customer",
            name="longitude",
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name="RideRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pickup_location", models.CharField(max_length=100)),
                ("dropoff_location", models.CharField(max_length=100)),
                ("status", models.CharField(default="pending", max_length=20)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Booking",
        ),
    ]
