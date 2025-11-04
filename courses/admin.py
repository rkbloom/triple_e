from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'duration', 'enrolled_count', 'created_at']
    list_filter = ['created_at', 'price']
    search_fields = ['title', 'description']
    filter_horizontal = ['enrolled_users']
    ordering = ['-created_at']
