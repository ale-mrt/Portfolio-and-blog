from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.order_by("-date")[:6]
    dropdownProjects = Project.objects.order_by("-date")[:3]
    return render(request, "portfolio/home.html", {"projects":projects, "dropdownProjects": dropdownProjects})

def portfolio_archive(request):
    projects = Project.objects.order_by("-date")[:6]
    dropdownProjects = Project.objects.order_by("-date")[:3]
    return render(request, "portfolio/portfolio_archive.html", {"projects":projects, "dropdownProjects": dropdownProjects})
    
def project(request, project_id):
    projects = Project.objects.order_by("-date")[:6]
    dropdownProjects = Project.objects.order_by("-date")[:3]
    return render(request, "portfolio/home.html", {"projects":projects, "dropdownProjects": dropdownProjects})

def bio(request):
    return render(request, "portfolio/bio.html")