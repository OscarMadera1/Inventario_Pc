"""importando models"""
from django.db import models

# Create your models here.

class MemoriaRam(models.Model):
    """memoria ram"""
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length = 15)
    capacidad = models.CharField(max_length = 15)

    def __str__(self):
        return f"{self.tipo} {self.capacidad} GB "

class DiscoDuro(models.Model):
    """clase disco duro"""
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length = 100)
    capacidad = models.FloatField(max_length = 20)

    def __str__(self):
        if self.capacidad<=1:
            return f"{self.marca} {self.capacidad} TB "
        else:
            return f"{self.marca} {self.capacidad} GB "


class Procesador(models.Model):
    """clase procesador"""
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length = 15)
    capacidad = models.CharField(max_length = 15)

    def __str__(self):
        return f"{self.tipo} {self.capacidad} "

class Computador(models.Model):
    """esta clase es para instaciar los equipos de compoto registrados"""
    id = models.AutoField(primary_key=True)
    serial = models.IntegerField(max_length = 50)
    marca = models.CharField(max_length = 100)
    ram = models.ForeignKey(MemoriaRam, null = False, blank = False, on_delete=models.CASCADE)
    disco = models.ForeignKey(DiscoDuro, null = False, blank = False, on_delete=models.CASCADE)
    procesador = models.ForeignKey(
        Procesador, null = False, blank = False, on_delete=models.CASCADE)    
    def __str__(self):
        return f"{self.serial} {self.marca} "

class Tecnico(models.Model):
    """Esta clase permite crear intancias de los tecnicos que realizan los mantenimientos"""

    documento = models.IntegerField(max_length = 15, primary_key = True)
    nombres = models.CharField(max_length = 150)
    apellidos = models.CharField(max_length = 250)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} "
    
class Mantenimiento(models.Model):
    """Mantenimientos realizados a los computaadores"""
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    tecnico = models.ForeignKey(Tecnico, null = False, blank = False, on_delete=models.CASCADE)
    computador = models.ForeignKey(
        Computador, null = False, blank = False, on_delete=models.CASCADE)
    def __str__(self):
        return f"Fecha: {self.fecha} Tecnico: {self.tecnico} Equipo: {self.computador} "