from tco_app.models import SystemTable, ModelTable, LicenceTable, CpuTable, CurrencyTable, CpuValueTable, MemoryValueTable
import pandas as pd 

file = pd.read_csv('newcputable.csv')
file
file['id_cpu_value_id']

file = open('newcputable.csv', 'r')
lines = file.readlines()[1:]
for line in lines:
  names = line.split(',')
  print(names)
  id_cpu_value_id  = str(names[0])
  id_memory_value_id = str(names[1])
  m = ModelTable()
  m.id = str(names[2])
  l = LicenceTable()
  l.id = str(names[3])
  newcpu = CpuTable(id_cpu_value_id=id_cpu_value_id, id_memory_value_id=id_memory_value_id, id_model=m, id_licence=l)
  newcpu.save()

cpus_val = CpuTable.objects.filter(id_model=28)
for cpu in cpus_val:
  print(cpu.id_cpu_value)



