# Generated by Django 4.2 on 2023-05-01 15:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("membership", "0004_alter_member_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="cf",
            field=models.CharField(
                blank=True,
                help_text="Codice Fiscale",
                max_length=16,
                verbose_name="Codice Fiscale",
            ),
        ),
        migrations.AlterField(
            model_name="member",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]