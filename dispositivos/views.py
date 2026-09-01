from django.shortcuts import render
from django.http import HttpResponse

def cargar_dispositivos():
    """Función auxiliar para obtener el listado de dispositivos."""
    return [
        {"nombre": "Medidor inteligente", "estado": "Activo", "consumo_kwh": 45.2},
        {"nombre": "Sensor de temperatura", "estado": "Activo", "consumo_kwh": 12.0},
        {"nombre": "Climatizador", "estado": "Revisión", "consumo_kwh": 120.5},
    ]

def inicio(request):
    contexto = {
        "sistema": "EcoEnergy",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
    }
    return render(request, "dispositivos/inicio.html", contexto)

def dispositivos_zona(request, zona_id):
    if zona_id != 3:
        return HttpResponse("Zona no encontrada", status=404)
    return HttpResponse(f"Dispositivos de la zona {zona_id}")

def catalogo(request):
    dispositivos = cargar_dispositivos()
    
    activos = sum(1 for item in dispositivos if item["estado"] == "Activo")
    
    contexto = {
        "dispositivos": dispositivos,
        "total": len(dispositivos),
        "total_activos": activos,
    }
    return render(request, "dispositivos/catalogo.html", contexto)
