from django.urls import path
from django.conf.urls import url
from . import views
from .views import all_json_models

urlpatterns = [
    # path('', views.index, name='index-page'),
    path('', views.system_choice, name='sims-page'),
    path('simulation_page', views.system_choice, name='sims-page'),
    path('simulation_page/<int:pk>/all_json_models/', views.all_json_models, name='all_json_models'),
    path('simulation_page/<int:pk>/all_json_cpus/', views.all_json_cpus, name='all_json_cpus'),
    path('simulation_page/<int:cpu>/<int:f_maintenance>/<str:currency>/json_simulation/', views.json_simulation, name='json_simulation'),
]