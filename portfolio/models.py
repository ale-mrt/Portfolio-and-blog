from django.db import models
import uuid
from datetime import datetime

# modello del progetto da convertire in query per il database
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(blank=True, upload_to="portfolio/images")
    url = models.URLField(blank=True)
    text = models.TextField(default="")
    date = models.DateTimeField(default=datetime.now())
