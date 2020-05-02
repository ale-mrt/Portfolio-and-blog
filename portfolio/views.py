from django.shortcuts import render, get_object_or_404
from .models import Project

# view della home. restituisce gli ultimi sei progetti per la visualizzazione nella pagina e gli ultimi tre per la visualizzazione nel bottone di dropdown
def home(request):
    projects = Project.objects.order_by("-date")[:6]
    dropdownProjects = Project.objects.order_by("-date")[:3]
    return render(request, "portfolio/home.html", {"projects": projects, "dropdownProjects": dropdownProjects})

# view dell'archivio. restituisce tutti i progetti per la visualizzazione nella pagina e gli ultimi tre per la visualizzazione nel bottone di dropdown
def portfolio_archive(request):
    projects = Project.objects.order_by("-date")
    dropdownProjects = Project.objects.order_by("-date")[:3]
    return render(request, "portfolio/portfolio_archive.html", {"projects":projects, "dropdownProjects": dropdownProjects})

# view del singolo progetto. restituisce gli ultimi tre progetti per la visualizzazione nel bottone di dropdwon e il progetto ottenuto col suo id
def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    dropdownProjects = Project.objects.order_by("-date")[:3]
    return render(request, "portfolio/project.html", {"project":project, "dropdownProjects": dropdownProjects})

# view della biografia: restituisce la pagina della biografia
def bio(request):
    return render(request, "portfolio/bio.html")