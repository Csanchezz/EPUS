from __future__ import unicode_literals
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

class Etiqueta(models.Model):
    COLOR_CHOICES = (
        ('navy', 'azul'),
        ('aqua', 'aqua'),
        ('purple', 'Morado'),
        ('yellow', 'Amarillo'),
        ('teal', 'turquesa'),
        ('red', 'rojo'),
        ('green', 'verde'),)

    etiqueta = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    color = models.CharField(default='purple', choices=COLOR_CHOICES, max_length=10)

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ('etiqueta',)

    def __str__(self):
        return self.etiqueta
class Publicacion(models.Model):
    titulo = models.CharField(max_length=50, blank = False)
    parrafo = models.TextField(blank=False, null=False)
    etiquetas = models.ManyToManyField(Etiqueta, related_name='publicacion')
    foto = ThumbnailerImageField(
        upload_to = 'post_image',
        blank=True,
        editable=True,)
    objects = models.Manager()
    def __str__(self):
        return self. titulo
