from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Institucion(models.Model):
    """
    Modelo para almacenar información de instituciones.
    """
    nombre = models.CharField(max_length=80, verbose_name="Nombre de la Institución", help_text="Máximo 80 caracteres.")
    direccion = models.CharField(max_length=255, verbose_name="Dirección", help_text="Ingrese la dirección completa.")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono", help_text="Número de contacto.")

    def __str__(self):
        return self.nombre


class Inscripcion(models.Model):
    """
    Modelo para almacenar las inscripciones al sistema.
    """
    ESTADOS = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO ASISTEN', 'No Asisten'),
    ]

    nombre = models.CharField(max_length=100, verbose_name="Nombre Completo", help_text="Ingrese el nombre completo del participante.")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono", help_text="Ingrese el número de contacto del participante.")
    email = models.EmailField(verbose_name="Correo Electrónico", help_text="Ingrese un correo electrónico válido.")
    numero_personas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)], verbose_name="Número de Personas", help_text="Cantidad de personas entre 1 y 30.")
    fecha_inscripcion = models.DateField(default=timezone.now, verbose_name="Fecha de Inscripción", help_text="Se asigna automáticamente la fecha actual.")
    hora_inscripcion = models.DateTimeField(default=timezone.now, verbose_name="Hora de Inscripción", help_text="Se asigna automáticamente la hora actual.")
    estado = models.CharField(max_length=20, choices=ESTADOS, verbose_name="Estado", help_text="Seleccione el estado de la inscripción.")
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, verbose_name="Institución", help_text="Seleccione la institución correspondiente.")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones", help_text="Puede dejar este campo en blanco.")

    def __str__(self):
        return f"{self.nombre} - {self.institucion.nombre}"

    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
        ordering = ['-fecha_inscripcion', '-hora_inscripcion']
