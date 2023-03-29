from django.db import models
from ckeditor.fields import RichTextField


class Project(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título")
    description = RichTextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen")
    url = models.URLField(verbose_name="URL", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")    
    
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]    
    
    
    def __str__(self):
        return self.title