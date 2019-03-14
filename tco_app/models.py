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

class CpuValueTable(models.Model):
    cpu_value = models.CharField(max_length=30, default='0')

    def __str__(self):
        return '{}'.format(self.cpu_value)

    def __repr__(self):
        return '{}'.format(self.cpu_value)

class MemoryValueTable(models.Model):
    memory_value = models.CharField(max_length=30, default='0')

    def __str__(self):
        return '{}'.format(self.memory_value)

    def __repr__(self):
        return '{}'.format(self.memory_value)

class CpuTable(models.Model):
    id_model = models.ForeignKey(ModelTable, on_delete=models.CASCADE)
    id_licence = models.ForeignKey(LicenceTable, on_delete=models.CASCADE)
    id_cpu_value = models.ForeignKey(CpuValueTable, on_delete=models.CASCADE, default=0)
    id_memory_value = models.ForeignKey(MemoryValueTable, on_delete=models.CASCADE, default=0) 

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.id_model, self.id_licence, self.id_cpu_value, self.id_memory_value)

    def __repr__(self):
        return '{} - {} CPU, {} MB '.format(self.id_model, self.id_cpu_value, self.id_memory_value)

class CurrencyTable(models.Model):
    country = models.CharField(max_length=50)
    iso_code = models.CharField(max_length=10)
    locale_code = models.CharField(max_length=50)

    def __str__(self):
        return '{}, ISO CODE: {}, LOCALE: {}'.format(self.country, self.iso_code, self.locale_code)
