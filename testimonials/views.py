from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Testimonial


def testimonial_list(request):
    """Testimonial listing with filtering"""
    testimonials = Testimonial.objects.filter(approved=True)

    # Filter by featured
    featured_filter = request.GET.get('featured', '')
    if featured_filter == 'true':
        testimonials = testimonials.filter(featured=True)

    # Pagination
    paginator = Paginator(testimonials, 12)  # 12 testimonials per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'featured_filter': featured_filter,
    }
    return render(request, 'testimonials/testimonial_list.html', context)
