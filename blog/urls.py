from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name="blog"

urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path("<int:post_id>/", views.post, name="post"),
    path("archive", views.blog_archive, name="blog_archive"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)