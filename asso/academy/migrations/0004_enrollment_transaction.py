# Generated by Django 4.2 on 2023-04-20 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accountant", "0001_initial"),
        ("academy", "0003_alter_session_options_remove_session_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="enrollment",
            name="transaction",
            field=models.OneToOneField(
                help_text="The Event of witch the Enrollment is referred to",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transaction_enrollment",
                to="accountant.transaction",
                verbose_name="Event",
            ),
        ),
    ]