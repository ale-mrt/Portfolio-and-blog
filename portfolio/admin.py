from django.contrib import admin
from .models import Project

# registrazione nel db del modello progetto
admin.site.register(Project)