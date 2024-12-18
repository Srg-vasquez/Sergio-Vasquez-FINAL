from django.urls import path
from .views import (
    ListarInscripcionesView,
    DetalleInscripcionView,
    AgregarInscripcionView,
    EditarInscripcionView,
    EliminarInscripcionView,
    api_instituciones,
    buscar_institucion,
    api_autor,  # Nueva API para datos del autor
    index
)

# Definición de rutas
urlpatterns = [
    # ===================== PÁGINA PRINCIPAL =====================
    path('', index, name='index'),  

    # ===================== INSCRIPCIONES (CBV) =====================
    path('listar/', ListarInscripcionesView.as_view(), name='listar_inscripciones'),
    path('detalle/<int:pk>/', DetalleInscripcionView.as_view(), name='detalle_inscripcion'),
    path('agregar/', AgregarInscripcionView.as_view(), name='agregar_inscripcion'),
    path('editar/<int:pk>/', EditarInscripcionView.as_view(), name='editar_inscripcion'),
    path('eliminar/<int:pk>/', EliminarInscripcionView.as_view(), name='eliminar_inscripcion'),

    # ===================== API DE INSTITUCIONES (FBV) =====================
    path('instituciones/', api_instituciones, name='api_instituciones'),
    path('instituciones/<int:id>/', buscar_institucion, name='buscar_institucion'),

    # ===================== API DE AUTOR =====================
    path('autor/', api_autor, name='api_autor'),
]
