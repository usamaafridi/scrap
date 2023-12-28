# Generated by Django 4.2.3 on 2023-12-27 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0007_rename_actual_quantity_order_assessed_amount_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="employee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="employee",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="assessed_amount",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="assessed_quantity",
            field=models.FloatField(blank=True, null=True),
        ),
    ]