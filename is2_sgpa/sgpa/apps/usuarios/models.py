from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ci = models.PositiveIntegerField(
        null=False,
        blank=False,
        unique=True,
        error_messages={"unique": "CI no disponible"},
    )
    roles = models.ManyToManyField(to="proyectos.Rol") #roles
    telefono = models.PositiveIntegerField(blank=False, null=True) #telefono

    class Meta:
        ordering = ["id"]
        permissions = (
            ("autorizar_usuario", "Permite la administración del SGPA"),
            ("acceso_usuario", "Permite el acceso a SGPA"),
            ("editar_usuario", "Permite editar usuario"),
            ("eliminar_usuario", "Permite eliminar usuario"),
        )

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name) #return
