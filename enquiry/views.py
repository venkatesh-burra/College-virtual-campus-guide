"""
Enquiry app views — admission enquiry form.
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EnquiryForm


def enquiry_form(request):
    """Handle enquiry form display and submission."""
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your enquiry has been submitted successfully.')
            return redirect('enquiry')
    else:
        form = EnquiryForm()

    return render(request, 'enquiry/enquiry_form.html', {'form': form})
