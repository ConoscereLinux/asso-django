# Generated by Django 4.2.1 on 2023-06-07 11:58

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("membership", "0011_member_come_from_member_interests_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="document_expires",
            field=models.DateField(
                default=datetime.date.today, verbose_name="Document Expiration Date"
            ),
        ),
        migrations.AlterField(
            model_name="member",
            name="phone",
            field=models.CharField(
                help_text="Phone Number, use only digits, +, -, space and parenthesis",
                max_length=50,
                validators=[
                    django.core.validators.RegexValidator(
                        "^(00|\\+)?((\\d+|\\(\\d+\\))[ \\-]?)+\\d$",
                        "Use only plus sign (at start), dashes (-), spaces and parenthesis",
                    )
                ],
                verbose_name="Phone Number",
            ),
        ),
    ]
