from django.shortcuts import render
from .models import About
from .forms import CollaborateForm
from django.contrib import messages


def about_me(request):
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate = collaborate_form.save(commit=False)
            collaborate.author = request.user
            collaborate.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
                )
        
    about = About.objects.all().order_by('created_on').first()
    collaborate_form = CollaborateForm()
    

    return render(
        request,
        "about/about.html",
        {"about": about,
        "collaborate_form": collaborate_form
        },
    )