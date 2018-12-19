from django.db import models
# from django. import serializers

# Create your models here.
class SystemTable(models.Model):
    system_name = models.CharField(max_length=50)

    def __str__(self):
        return self.system_name

class ModelTable(models.Model):
    model_name = models.CharField(max_length=50)
    power_name = models.CharField(max_length=50)
    power_watt = models.IntegerField(default=0)    
    id_system = models.ForeignKey(SystemTable, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name

class LicenceTable(models.Model):
    licence_name = models.CharField(max_length=50)
    licence_cost = models.IntegerField(default=0)

    def __str__(self):
        return self.licence_name

class CpuTable(models.Model):
    min_cpu = models.IntegerField(default=0)
    max_cpu = models.IntegerField(default=0)
    id_model = models.ForeignKey(ModelTable, on_delete=models.CASCADE)
    id_licence = models.ForeignKey(LicenceTable, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_model) + ' ' + str(self.min_cpu) + ' - ' + str(self.max_cpu) + ' CPU'
        # return self.id_model + ' ' + self.min_cpu + ' - ' + self.max_cpu + ' CPU'

class CurrencyTable(models.Model):
    country = models.CharField(max_length=50)
    iso_code = models.CharField(max_length=10)
    locale_code = models.CharField(max_length=50)

    def __str__(self):
        return str(self.country) + ', ' + str(self.iso_code) + ', ' + str(self.locale_code)
