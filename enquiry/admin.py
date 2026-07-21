from django.contrib import admin
from .models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'email', 'phone', 'course', 'city', 'created_at')
    list_filter = ('course', 'created_at')
    search_fields = ('student_name', 'email', 'city')
    readonly_fields = ('created_at',)
