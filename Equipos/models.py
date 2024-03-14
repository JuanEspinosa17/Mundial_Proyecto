from django.db import models

# Create your models here.

#TABLA ESTADO
class estado(models.Model):
    estado = models.CharField(max_length=10, verbose_name='Estado')
    
    def __str__(self):
        return self.estado
    
    class Meta:
        verbose_name='Estado'
        verbose_name_plural='Estados'
        db_table='estado'
        ordering=['id']
        
    
#TABLA NACIONALIDAD
class nacionalidad(models.Model):
    nacionalidad = models.CharField(max_length=20, verbose_name='Nacionalidad')
    
    def __str__(self):
        return self.nacionalidad
    
    class Meta:
        verbose_name='Nacionalidad'
        verbose_name_plural='Nacionalidades'
        db_table='nacionalidad'
        ordering=['id']

#TABLA ROL
class rol(models.Model):
    rol = models.CharField(max_length=15, verbose_name='Rol')
    
    def __str__(self):
        return self.rol
    
    class Meta:
        verbose_name='Rol'
        verbose_name_plural='Roles'
        db_table='rol'
        ordering=['id']
        
#TABLA EQUIPO
class equipo(models.Model):
    nombre = models.CharField(max_length=15, verbose_name='Nombre')
    bandera = models.CharField(max_length=1000, verbose_name='Bandera')
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name='Equipo'
        verbose_name_plural='Equipos'
        db_table='equipo'
        ordering=['id']
        
#TABLA JUGADOR
class jugador(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    apellido = models.CharField(max_length=20, verbose_name='Apellido')
    fecha_nacimiento = models.DateField(verbose_name='Fecha_Nacimiento', null=True, blank=True)
    num_camisa = models.IntegerField(verbose_name='Num_Camisa', null=True, blank=True)
    idestado = models.ForeignKey(estado, on_delete=models.CASCADE)
    idnacionalidad = models.ForeignKey(nacionalidad, on_delete=models.CASCADE)
    idequipo = models.ForeignKey(equipo, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name='Jugador'
        verbose_name_plural='Jugadores'
        db_table='jugador'
        ordering=['id']
        
#TABLA TECNICO
class tecnico(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    apellido = models.CharField(max_length=20, verbose_name='Apellido')
    fecha_nacimiento = models.DateField(verbose_name='Fecha_Nacimiento')
    idrol = models.ForeignKey(rol, on_delete=models.CASCADE)
    idnacionalidad = models.ForeignKey(nacionalidad, on_delete=models.CASCADE)
    idequipo = models.ForeignKey(equipo, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name='Tecnico'
        verbose_name_plural='Tecnicos'
        db_table='tecnico'
        ordering=['id']