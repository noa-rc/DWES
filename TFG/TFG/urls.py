from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('contacto/', views.contacto, name='contacto'),
    path('showcase/', include('showcase.urls')),
    path('calendario/', include('calendario.urls')),
    path('tres-en-raya/', include('tres_en_raya.urls')),
]