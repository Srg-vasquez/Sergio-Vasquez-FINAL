from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.utils.timezone import now
from .models import Inscripcion, Institucion
from .forms import FormInscripcion
from django.contrib import messages
from django.core.management import call_command
import logging
from django import forms
from .models import Institucion
from .forms import FormInstitucion


# Configurar logging para errores
logger = logging.getLogger(__name__)

# ======================= PÁGINA PRINCIPAL =======================
def index(request):
    """
    Renderiza la página principal.
    """
    return render(request, 'index.html')

def cargar_instituciones(request):
    """
    Carga 15 instituciones predefinidas en la base de datos si no existen.
    """
    instituciones_predefinidas = [
        {"nombre": "Universidad de Chile", "direccion": "Av. Libertador Bernardo O'Higgins 1058", "telefono": "223334445"},
        {"nombre": "Pontificia Universidad Católica de Chile", "direccion": "Av. Vicuña Mackenna 4860", "telefono": "223334446"},
        {"nombre": "Universidad de Santiago", "direccion": "Av. Ecuador 3659", "telefono": "223334447"},
        {"nombre": "Universidad de Valparaíso", "direccion": "Av. Errázuriz 1834", "telefono": "223334448"},
        {"nombre": "Universidad de Concepción", "direccion": "Edmundo Larenas 10", "telefono": "223334449"},
        {"nombre": "Universidad Técnica Federico Santa María", "direccion": "Av. España 1680", "telefono": "223334450"},
        {"nombre": "Universidad Austral de Chile", "direccion": "Independencia 641", "telefono": "223334451"},
        {"nombre": "Universidad de La Frontera", "direccion": "Francisco Salazar 1145", "telefono": "223334452"},
        {"nombre": "Universidad Católica de Valparaíso", "direccion": "Av. Brasil 2950", "telefono": "223334453"},
        {"nombre": "Universidad de Talca", "direccion": "Av. Lircay S/N", "telefono": "223334454"},
        {"nombre": "Universidad Andrés Bello", "direccion": "República 239", "telefono": "223334455"},
        {"nombre": "Universidad de Los Lagos", "direccion": "Camino a Chinquihue Km. 6", "telefono": "223334456"},
        {"nombre": "Universidad de Atacama", "direccion": "Av. Copayapu 485", "telefono": "223334457"},
        {"nombre": "Universidad del Bío-Bío", "direccion": "Av. Collao 1202", "telefono": "223334458"},
        {"nombre": "Universidad Adolfo Ibáñez", "direccion": "Diagonal Las Torres 2640", "telefono": "223334459"},
    ]

    for institucion in instituciones_predefinidas:
        Institucion.objects.get_or_create(**institucion)
    
    messages.success(request, "Se han cargado las instituciones por defecto.")
    return redirect('index')

# ======================= INSCRIPCIONES =======================
class ListarInscripcionesView(ListView):
    """
    Vista para listar todas las inscripciones.
    """
    model = Inscripcion
    template_name = 'listar_inscripciones.html'
    context_object_name = 'inscripciones'
    paginate_by = 10

class DetalleInscripcionView(DetailView):
    """
    Vista para ver el detalle de una inscripción.
    """
    model = Inscripcion
    template_name = 'detalle_inscripcion.html'
    context_object_name = 'inscripcion'

class AgregarInscripcionView(CreateView):
    """
    Vista para agregar una nueva inscripción.
    """
    model = Inscripcion
    form_class = FormInscripcion
    template_name = 'agregar_inscripcion.html'
    success_url = reverse_lazy('listar_inscripciones')

    def form_valid(self, form):
        """
        Valida y guarda la inscripción si el formulario es válido.
        """
        messages.success(self.request, "Inscripción agregada correctamente.")
        logger.info("Inscripción guardada con éxito.")
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Maneja errores cuando el formulario no es válido.
        """
        logger.error(f"Errores al guardar inscripción: {form.errors}")
        messages.error(self.request, "Ocurrió un error al guardar la inscripción.")
        return self.render_to_response(self.get_context_data(form=form))

class EditarInscripcionView(UpdateView):
    """
    Vista para editar una inscripción existente.
    """
    model = Inscripcion
    form_class = FormInscripcion
    template_name = 'editar_inscripcion.html'
    success_url = reverse_lazy('listar_inscripciones')

    def form_valid(self, form):
        """
        Actualiza la fecha y hora de inscripción al guardar cambios.
        """
        form.instance.fecha_inscripcion = now().date()
        form.instance.hora_inscripcion = now()
        messages.success(self.request, "Inscripción editada correctamente.")
        logger.info("Inscripción actualizada con éxito.")
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Maneja errores al editar una inscripción.
        """
        logger.error(f"Errores al editar inscripción: {form.errors}")
        messages.error(self.request, "Ocurrió un error al editar la inscripción.")
        return self.render_to_response(self.get_context_data(form=form))

class EliminarInscripcionView(View):
    """
    Vista para eliminar una inscripción mediante solicitud POST.
    """
    def post(self, request, id):
        try:
            # Obtiene la inscripción por ID
            inscripcion = get_object_or_404(Inscripcion, id=id)
            inscripcion.delete()  # Elimina la inscripción
            logger.info(f"Inscripción con ID {id} eliminada correctamente.")
            messages.success(request, "Inscripción eliminada correctamente.")
            return redirect('listar_inscripciones')  # Redirige a la lista de inscripciones
        except Inscripcion.DoesNotExist:
            logger.error(f"Inscripción con ID {id} no encontrada.")
            messages.error(request, "La inscripción no fue encontrada.")
            return redirect('listar_inscripciones')  # Redirige en caso de error
        except Exception as e:
            logger.error(f"Error inesperado al eliminar inscripción: {str(e)}")
            messages.error(request, "Error inesperado al eliminar la inscripción.")
            return redirect('listar_inscripciones')


# ======================= APIS =======================
def api_instituciones(request):
    """
    API que devuelve la lista de instituciones en formato JSON.
    """
    try:
        instituciones = Institucion.objects.all().values('id', 'nombre', 'direccion', 'telefono')
        return JsonResponse({'status': 'success', 'data': list(instituciones)}, safe=False)
    except Exception as e:
        logger.error(f"Error al obtener instituciones: {str(e)}")
        return JsonResponse({'status': 'error', 'message': 'Error al obtener las instituciones'}, status=500)

def buscar_institucion(request, id):
    """
    API para buscar una institución por su ID.
    """
    try:
        institucion = get_object_or_404(Institucion, id=id)
        return JsonResponse({'status': 'success', 'data': {
            'id': institucion.id,
            'nombre': institucion.nombre,
            'direccion': institucion.direccion,
            'telefono': institucion.telefono
        }}, status=200)
    except Exception as e:
        logger.error(f"Error al buscar institución: {str(e)}")
        return JsonResponse({'status': 'error', 'message': 'No se encontró la institución.'}, status=404)

def api_autor(request):
    """
    API que devuelve información del autor del proyecto.
    """
    datos_autor = {
        "nombre": "Sergio Vásquez",
        "email": "srg.jvasquez@gmail.com",
        "proyecto": "Sergio_Vasquez_FINAL",
        "descripcion": "Examen final en la asignatura BACK-END",
        "url": "https://github.com/Srg-vasquez/Sergio-Vasquez-FINAL"
    }
    return JsonResponse({'status': 'success', 'data': datos_autor})



def agregar_institucion(request):
    """
    Vista para agregar una nueva institución.
    """
    if request.method == 'POST':
        form = FormInstitucion(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Institución agregada correctamente.")
            return redirect('index') 
        else:
            messages.error(request, "Ocurrió un error al agregar la institución.")
    else:
        form = FormInstitucion()

    return render(request, 'agregar_institucion.html', {'form': form})


class FormInstitucion(forms.ModelForm):
    """
    Formulario para agregar y editar instituciones.
    """
    class Meta:
        model = Institucion
        fields = ['nombre', 'direccion', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la institución'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono'
            }),
        }