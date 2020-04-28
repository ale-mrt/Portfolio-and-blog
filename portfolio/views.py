from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.order_by("-date")[:6]
    dropdownProjects = Project.objects.order_by("-date")[:3]
    return render(request, "portfolio/home.html", {"projects":projects, "dropdownProjects": dropdownProjects})

def portfolio_archive(request):
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio_archive.html", {"projects":projects})
    