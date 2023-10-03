# Generated by Django 4.2.5 on 2023-10-02 21:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("academy", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="need_membership",
            field=models.BooleanField(
                default=True,
                help_text="Indicate if the membership is needed in order to attend to this event",
                verbose_name="Membership Needed",
            ),
        ),
    ]