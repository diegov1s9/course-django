from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    # Permite mostrar el titulo en la lista de post en la vista de admin
    def __str__(self):
        """
        Devuelve una representación legible del objeto Post.
        Esto es útil para mostrar un nombre significativo en la interfaz de administración
        de Django y en otras partes donde se necesite una representación de cadena del objeto.
        """
        return self.title
