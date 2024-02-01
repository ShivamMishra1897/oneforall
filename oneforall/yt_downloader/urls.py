from django.urls import path
from .import views

urlpatterns = {
    path('dwnl',views.youtube_downloader,name='dwnl'),
}