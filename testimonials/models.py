from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Testimonial(models.Model):
    """
    Testimonial model for user reviews and testimonials
    """
    SOURCE_CHOICES = [
        ('video', 'Video'),
        ('text', 'Text'),
        ('audio', 'Audio'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='testimonials',
        null=True,
        blank=True
    )
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name='testimonials'
    )
    user_name = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=5
    )
    source = models.CharField(
        max_length=10,
        choices=SOURCE_CHOICES,
        default='text'
    )
    source_url = models.CharField(max_length=255, blank=True, null=True)
    approved = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'testimonials'
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['-date']

    def __str__(self):
        return f"{self.user_name} - {self.course.title}"
