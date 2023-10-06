from django.contrib import admin


class TimeStampAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """
        Update created_by and edited_by model

        Based upon:
        https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
        """
        if obj.pk is None:
            obj.created_by = request.user
        obj.updated_by = request.user

        super().save_model(request, obj, form, change)


class ContentAdmin(TimeStampAdmin):
    pass
