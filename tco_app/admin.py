from django.contrib import admin
from .models import SystemTable, ModelTable, LicenceTable, CpuTable, CurrencyTable

admin.site.register(SystemTable)
admin.site.register(LicenceTable)
admin.site.register(ModelTable)
admin.site.register(CpuTable)
admin.site.register(CurrencyTable)
