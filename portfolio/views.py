from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.order_by("-date")[:6]
    dropdownProjects = Project.objects.order_by("-date")[:3]
    return render(request, "portfolio/home.html", {"projects":projects, "dropdownProjects": dropdownProjects})

def portfolio_archive(request):
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio_archive.html", {"projects":projects})
    
def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, "portfolio/project.html", {"project": project})

def base(request):
    return render(request, "portfolio/base.html")