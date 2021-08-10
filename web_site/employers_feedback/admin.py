from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'text']
    verbose_name = 'предложения'


# Register your models here.
admin.site.register(Feedback, FeedbackAdmin)

# Register your models here.
