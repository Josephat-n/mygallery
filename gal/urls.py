from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
   path('', views.home, name ='gallery-home'),
   path('search/', views.search_results, name='search_results')
]


if settings.DEBUG:
   urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)