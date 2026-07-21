"""
URL patterns for enquiry app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.enquiry_form, name='enquiry'),
]
