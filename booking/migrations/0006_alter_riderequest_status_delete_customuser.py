# Generated by Django 5.0.6 on 2024-05-10 09:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0005_customuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="riderequest",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("accepted", "Accepted"),
                    ("rejected", "Rejected"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
