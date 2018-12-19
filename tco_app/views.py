from django.shortcuts import render
from django.http import HttpResponse
from .models import SystemTable, ModelTable, LicenceTable, CpuTable, CurrencyTable
from django.core import serializers
import json
import sys
import requests
import locale

def index(request):
    # context = {
    #     'systems': SystemTable.objects.all()
    # }

    return render(request, 'tco_app/index.html')
    # return HttpResponse("Homepage")

def modelsNames(request):
    context = {
        'models': ModelTable.objects.all()
    }

    return render(request, "tco_app/teste.html", context)

def system_choice(request):
    context = {
        'systems': SystemTable.objects.all(),
        'currency': CurrencyTable.objects.all()
    }
    return render(request, "tco_app/simulation.html", context)

def all_json_models(request, pk):
    # id_system = ModelTable.objects.get(id_system=systemid)
    models = ModelTable.objects.all().filter(id_system=pk)
    # sys.stderr.write('*********************: ' + 
    # str(ModelTable.objects.all().filter(id_system=systemid).count()))
    json_models = serializers.serialize('json', models)
    return HttpResponse(json_models, content_type='application/javascript')

def all_json_cpus(request, pk):
    # sys.stderr.write('*********************: ' + pk)
    cpus = CpuTable.objects.all().filter(id_model=pk)
    json_cpus = serializers.serialize('json', cpus)
    return HttpResponse(json_cpus, content_type='application/javascript')

def json_simulation(request, cpu, f_maintenance, currency):
    ####### Constants ##########
    f_power_instance = 150
    f_carbon_footprint = 0.744
    f_support = 467
    i_generic_power = 350
    ####### Constants ##########

    ######## DB QUERIES ##########
    f_licence = LicenceTable.objects.filter(cputable__id=cpu)[0].licence_cost
    f_power = ModelTable.objects.filter(cputable__id=cpu)[0].power_watt 

    f_power = float(f_power)
    f_power_instance = float(f_power_instance)
    f_carbon_power_legacy = float((f_power / 1000)*(24*365)) # Yearly power Consumption of the legacy system
    f_carbon_power_instance = float((f_power_instance / 1000)*(24*365)) # Yearly power Consumption of the instance
    f_carbon_footprint_legacy = (f_carbon_power_legacy * f_carbon_footprint) # Yearly carbon footprint of the legacy system
    f_carbon_footprint_instance = (f_carbon_power_instance * f_carbon_footprint) # Yearly carbon footprint of the instance
    f_carbon_footprint_savings = (f_carbon_footprint_legacy - f_carbon_footprint_instance) # Yearly carbon footprint savings
    f_power_savings = (f_carbon_power_legacy - f_carbon_power_instance)# Yearly Power Savings
    
    ## Gets the currency exchange rate
    base = "EUR"
    
    if not currency == 'EUR':
        other = CurrencyTable.objects.filter(iso_code=currency)[0].iso_code
        res = requests.get("http://data.fixer.io/api/latest?access_key=5b82db35be8ceb9321ca7a1502f1d704",
                        params={"base": base, "symbols": other})
        if res.status_code != 200:
            raise Exception("ERROR: API request unsuccessful.")
        data = res.json()
        rate = float(data["rates"][other])

        f_licence = f_licence * rate
    
    locale_code = CurrencyTable.objects.filter(iso_code=currency)[0].locale_code
    locale.setlocale(locale.LC_ALL, locale_code)
    f_total_savings = (f_maintenance - (f_licence + f_support))
    f_total_savings_currency = (locale.currency(f_total_savings,grouping=True))

    # ?????????????
    # s_consumed_power = str(f_carbon_power_legacy)
    i_power_savings = round(f_power_savings)
    i_carbon_footprint_legacy = round(f_carbon_footprint_legacy)
    i_carbon_footprint_savings = round(f_carbon_footprint_savings)

    output_simulation = {}
    output_simulation['f_total_savings_currency'] = f_total_savings_currency
    output_simulation['reduction_of'] = str(round(100-(f_licence*100/f_maintenance))) + '%'
    output_simulation['i_power_savings'] = str(i_power_savings) + ' kWh/Year'
    output_simulation['i_carbon_footprint_legacy'] = str(i_carbon_footprint_legacy) + 'Kg of CO2'
    output_simulation['i_carbon_footprint_savings'] = str(i_carbon_footprint_savings) + 'Kg of CO2/Year'
    output_simulation['space_floor'] = '99.9%'

    return HttpResponse(json.dumps(output_simulation), content_type='application/javascript')
