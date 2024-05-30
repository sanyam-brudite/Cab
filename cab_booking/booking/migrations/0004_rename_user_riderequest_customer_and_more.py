# Generated by Django 5.0.6 on 2024-05-09 12:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0003_alter_customer_latitude_alter_customer_longitude_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="riderequest",
            old_name="user",
            new_name="customer",
        ),
        migrations.AlterField(
            model_name="riderequest",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("accepted", "Accepted"),
                    ("rejected", "Rejected"),
                ],
                max_length=20,
            ),
        ),
    ]
