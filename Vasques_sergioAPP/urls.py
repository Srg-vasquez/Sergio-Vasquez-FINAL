from django.urls import path
from .views import (
    ListarInscripcionesView,
    DetalleInscripcionView,
    AgregarInscripcionView,
    EditarInscripcionView,
    EliminarInscripcionView,
    api_instituciones,
    buscar_institucion,
    cargar_instituciones,
    agregar_institucion,
    api_autor,
    index
)

urlpatterns = [
    # Página principal
    path('', index, name='index'),

    # Inscripciones (CRUD)
    path('inscripciones/', ListarInscripcionesView.as_view(), name='listar_inscripciones'),
    path('inscripciones/detalle/<int:pk>/', DetalleInscripcionView.as_view(), name='detalle_inscripcion'),
    path('inscripciones/agregar/', AgregarInscripcionView.as_view(), name='agregar_inscripcion'),
    path('inscripciones/editar/<int:pk>/', EditarInscripcionView.as_view(), name='editar_inscripcion'),
    path('inscripciones/eliminar/<int:id>/', EliminarInscripcionView.as_view(), name='eliminar_inscripcion'),

    # APIs
    path('api/instituciones/', api_instituciones, name='api_instituciones'),
    path('api/instituciones/<int:id>/', buscar_institucion, name='buscar_institucion'),
    path('api/autor/', api_autor, name='api_autor'),


       # Ruta para cargar instituciones
    path('cargar_instituciones/', cargar_instituciones, name='cargar_instituciones'),

    #agregar instituciones
     path('instituciones/agregar/', agregar_institucion, name='agregar_institucion'),
]

