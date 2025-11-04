from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import FAQ, ContactMessage
from courses.models import Course
from testimonials.models import Testimonial


def home(request):
    """Homepage with conversion-driven design"""
    # Get featured courses and testimonials
    featured_courses = Course.objects.all()[:3]
    featured_testimonials = Testimonial.objects.filter(approved=True, featured=True)[:3]

    context = {
        'featured_courses': featured_courses,
        'featured_testimonials': featured_testimonials,
    }
    return render(request, 'pages/home.html', context)


def about(request):
    """About page"""
    return render(request, 'pages/about.html')


def faq(request):
    """FAQ page with expandable/collapsible answers"""
    faqs = FAQ.objects.filter(is_active=True)
    return render(request, 'pages/faq.html', {'faqs': faqs})


def contact(request):
    """Contact form with email notifications"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Send email notification (will print to console in development)
        try:
            send_mail(
                subject=f'Contact Form: {subject}',
                message=f'From: {name} ({email})\n\n{message}',
                from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@triplee.com',
                recipient_list=[settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'admin@triplee.com'],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Email error: {e}")

        messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
        return redirect('contact')

    return render(request, 'pages/contact.html')
