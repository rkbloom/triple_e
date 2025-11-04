from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'course', 'rating', 'source', 'approved', 'featured', 'date']
    list_filter = ['approved', 'featured', 'source', 'rating', 'date']
    search_fields = ['user_name', 'content', 'course__title']
    list_editable = ['approved', 'featured']
    ordering = ['-date']
