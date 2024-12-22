from django import forms
from .models import Inscripcion
from .models import Institucion

class FormInscripcion(forms.ModelForm):
    """
    Formulario para la creación y edición de inscripciones.
    """
    class Meta:
        model = Inscripcion
        fields = ['nombre', 'telefono', 'email', 'numero_personas', 'estado', 'institucion', 'observaciones']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre completo'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Teléfono de contacto'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Correo electrónico válido'
            }),
            'numero_personas': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Cantidad de personas'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'institucion': forms.Select(attrs={
                'class': 'form-select'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Observaciones (opcional)'
            }),
        }

    # Validación personalizada para el número de personas
    def clean_numero_personas(self):
        numero = self.cleaned_data.get('numero_personas')
        if numero < 1 or numero > 30:
            raise forms.ValidationError("El número de personas debe estar entre 1 y 30.")
        return numero

    # Validación personalizada para el email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("El correo electrónico es obligatorio.")
        return email

    # Validación personalizada para el teléfono
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono.isdigit():
            raise forms.ValidationError("El teléfono solo debe contener números.")
        return telefono


class FormInstitucion(forms.ModelForm):
    """
    Formulario para agregar una nueva institución.
    """
    class Meta:
        model = Institucion
        fields = ['nombre', 'direccion', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la institución'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
        }