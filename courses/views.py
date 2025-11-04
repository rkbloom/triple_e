from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Course


def course_list(request):
    """Course listing with pagination and search functionality"""
    courses = Course.objects.all()

    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        courses = courses.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # Pagination
    paginator = Paginator(courses, 9)  # 9 courses per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'courses/course_list.html', context)


def course_detail(request, pk):
    """Course detail page with enrollment option"""
    course = get_object_or_404(Course, pk=pk)
    is_enrolled = False

    if request.user.is_authenticated:
        is_enrolled = course.enrolled_users.filter(id=request.user.id).exists()

    # Get testimonials for this course
    testimonials = course.testimonials.filter(approved=True)[:5]

    context = {
        'course': course,
        'is_enrolled': is_enrolled,
        'testimonials': testimonials,
    }
    return render(request, 'courses/course_detail.html', context)


@login_required
def enroll_course(request, pk):
    """Enroll user in a course"""
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        if course.enrolled_users.filter(id=request.user.id).exists():
            messages.info(request, 'You are already enrolled in this course.')
        else:
            course.enrolled_users.add(request.user)
            messages.success(request, f'Successfully enrolled in {course.title}!')
            return redirect('accounts:dashboard')

    return redirect('courses:course_detail', pk=pk)
