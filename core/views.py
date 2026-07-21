"""
Core app views — Home, About, Gallery, Campus Tour, Contact pages.
"""
from django.shortcuts import render
from courses.models import Course
from .models import Gallery


def home(request):
    """Home page with hero banner and course highlights."""
    # Show first 4 courses on home page
    courses = Course.objects.all()[:4]
    return render(request, 'core/home.html', {'courses': courses})


def about(request):
    """About page with college information."""
    return render(request, 'core/about.html')


def gallery(request):
    """Gallery page — displays all uploaded images."""
    images = Gallery.objects.all()
    return render(request, 'core/gallery.html', {'images': images})


def campus_tour(request):
    """Campus tour page with YouTube video and facility cards."""
    return render(request, 'core/campus_tour.html')


def contact(request):
    """Contact page with address and map."""
    return render(request, 'core/contact.html')
