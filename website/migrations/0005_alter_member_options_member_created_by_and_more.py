# Generated by Django 4.1.7 on 2023-03-07 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("website", "0004_rename_name_member_first_name_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="member",
            options={"ordering": ["-creation_date"]},
        ),
        migrations.AddField(
            model_name="member",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The User that has created the object",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Creation User",
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="creation_date",
            field=models.DateTimeField(
                auto_now_add=True,
                default=None,
                help_text="The Date and the Time of creation on the object",
                verbose_name="Creation Date and Time",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="member",
            name="edit_date",
            field=models.DateTimeField(
                auto_now=True,
                help_text="The Date and the Time of last time the object was edited",
                verbose_name="Last edit Date and Time",
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="trash_state",
            field=models.BooleanField(
                default=False,
                help_text="Indicates if the object is trashed",
                verbose_name="Trashed",
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The User edited the object last time",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="updated_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Last edit User",
            ),
        ),
    ]