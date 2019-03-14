from django.contrib import admin
from .models import SystemTable, ModelTable, LicenceTable, CpuTable, CurrencyTable, CpuValueTable, MemoryValueTable

admin.site.register(SystemTable)
admin.site.register(LicenceTable)
admin.site.register(ModelTable)
admin.site.register(CpuTable)
admin.site.register(CurrencyTable)
admin.site.register(CpuValueTable)
admin.site.register(MemoryValueTable)
