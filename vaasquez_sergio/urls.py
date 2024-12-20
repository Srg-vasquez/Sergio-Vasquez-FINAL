from django.contrib import admin
from django.urls import path, include
from Vasques_sergioAPP import views  # Importa las vistas de la app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Página principal
    path('inscripciones/', include('Vasques_sergioAPP.urls')),  # Rutas para inscripciones y APIs
]
