# Generated by Django 4.2.1 on 2023-11-29 21:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_remove_personaldetails_phone_number_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="personaldetails",
            old_name="addres1",
            new_name="address1",
        ),
        migrations.RenameField(
            model_name="personaldetails",
            old_name="addres2",
            new_name="address2",
        ),
    ]