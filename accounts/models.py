from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from simple_history.models import HistoricalRecords

class Profile(models.Model):
    TIPO_CHOICES = [
        ('admin', 'Administrador'),
        ('empleado', 'Empleado'),
        ('cliente', 'Cliente'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_CHOICES, default='empleado')
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='profiles/', blank=True, null=True)
    history = HistoricalRecords()
    
    def __str__(self):
        return f"{self.user.username} - {self.get_tipo_usuario_display()}"

# Signal to create/update Profile when User is created/updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
