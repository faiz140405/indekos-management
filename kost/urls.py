# kost/urls.py
from django.urls import path
from . import views

app_name = 'kost' # Untuk namespacing URL

urlpatterns = [
    path('', views.daftar_kost, name='daftar_kost'),
    path('<int:kost_id>/', views.detail_kost, name='detail_kost'),
    path('tentang-kami/', views.tentang_kami, name='tentang_kami'),
    path('kontak/', views.kontak, name='kontak'),  
]