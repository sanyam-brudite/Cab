# Generated by Django 5.0.6 on 2024-05-12 06:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0011_alter_riderequest_customer"),
    ]

    operations = [
        migrations.RenameField(
            model_name="riderequest",
            old_name="customer",
            new_name="username",
        ),
    ]
