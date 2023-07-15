from django.db import models

# Create your models here.
class Edificio(models.Model):
    opciones_tipo_edificio = (
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial')
    )

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, choices=opciones_tipo_edificio)

    def __str__(self):
        return "Edificio: %s - %s - %s - %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)
    
    def get_nro_cuartos_total(self):
        cantidadTotal = [d.nro_cuartos for d in self.departamentos.all()]
        cantidadTotal = sum(cantidadTotal)
        return cantidadTotal
    
    def get_costo_total(self):
        costoTotal = [d.costo for d in self.departamentos.all()]
        costoTotal = sum(costoTotal)
        return costoTotal
    

class Departamento(models.Model):
    propietario = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits= 8, decimal_places= 2)
    nro_cuartos =  models.IntegerField("Número de cuartos")
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "Departamento: Propietario = %s - %f - Num. Cuartos = %d" % (self.propietario, 
                self.costo, 
                self.nro_cuartos)