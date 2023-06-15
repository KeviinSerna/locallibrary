from django.db import models

class Language(models.Model):
    
    name = models.CharField(max_length=50, help_text="Ingrese el lenguaje (ejm: Español, Ingles.)")

    def __str__(self):

        return self.name