from django.urls import path
from . import views

app_name = "dispositivos"

urlpatterns = [
    # Vista opcional de inicio/portada
    path("", views.inicio, name="inicio"),
    
    # Exigencia pauta: Listado de zonas (/zonas/)
    path("zonas/", views.lista_zonas, name="lista_zonas"),
    
    # Exigencia pauta: Detalle de zona (/zonas/<id>/)
    path("zonas/<int:zona_id>/", views.detalle_zona, name="detalle_zona"),
]


