# Generated by Django 5.0.6 on 2024-05-12 11:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0012_rename_customer_riderequest_username"),
    ]

    operations = [
        migrations.RenameField(
            model_name="riderequest",
            old_name="username",
            new_name="customer",
        ),
    ]
