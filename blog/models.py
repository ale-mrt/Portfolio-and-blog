from django.db import models
import datetime

# Create your models here.

# modello del post del blog
class Blog_post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    image = models.ImageField(blank=True, upload_to="portfolio/images")
