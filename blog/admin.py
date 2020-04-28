from django.contrib import admin
from .models import Blog_post

# registrazione del modello, ovvero dire al database di creare una nuova tavola
admin.site.register(Blog_post)