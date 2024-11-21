from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    content = RichTextField(verbose_name='Contenido')
    
    url = models.CharField(max_length=100)
    
    image = models.ImageField(verbose_name='Imagen', upload_to='proyect')
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta: 
        verbose_name = 'Pelicula'
        ordering = ['-created']
    
    def save(self) -> None:
        if self.url:
            self.url = self.url.replace(' ','-')
        return super().save()