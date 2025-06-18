# kost_management/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kost.urls')), # Ubah 'kost/' menjadi '' (path kosong)
]