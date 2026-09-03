import json
import os
from django.conf import settings
from django.shortcuts import render
from django.http import Http404

def cargar_json(nombre_archivo):
    """Carga dinámicamente cualquier archivo desde la carpeta /data/"""
    ruta = os.path.join(settings.BASE_DIR, 'data', nombre_archivo)
    with open(ruta, 'r', encoding='utf-8') as file:
        return json.load(file)

def inicio(request):
    """Vista opcional de portada"""
    contexto = {
        "sistema": "EcoEnergy",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
    }
    return render(request, "dispositivos/inicio.html", contexto)

def lista_zonas(request):
    """CA-01 y CA-02: Carga zonas y calcula la cantidad de dispositivos dinámicamente"""
    zonas = cargar_json('zonas.json')
    dispositivos = cargar_json('dispositivos.json')

    # Cuenta cuántos dispositivos pertenecen a cada zona
    for zona in zonas:
        zona['cant_dispositivos'] = sum(1 for d in dispositivos if d['zona_id'] == zona['id'])

    return render(request, 'dispositivos/zonas.html', {'zonas': zonas})

def detalle_zona(request, zona_id):
    """CA-03 a CA-08: Muestra consumo total, métricas, tipo de carga y estado ALERTA/NORMAL"""
    zonas = cargar_json('zonas.json')
    categorias = cargar_json('categorias.json')
    dispositivos = cargar_json('dispositivos.json')

    # CA-08: Buscar la zona. Si no existe, lanza Http404 controladamente
    zona = next((z for z in zonas if z['id'] == zona_id), None)
    if not zona:
        raise Http404("La zona solicitada no existe")

    # Mapeo id -> nombre de categoría (aplicación)
    cat_map = {c['id']: c['nombre'] for c in categorias}

    dispositivos_zona = []
    consumo_total = 0.0

    for d in dispositivos:
        if d['zona_id'] == zona_id:
            consumo = float(d['consumo_kwh'])
            consumo_total += consumo
            
            # Condición para marcar la carga del dispositivo
            es_peligrosa = consumo > (float(zona['limite_kwh']) * 0.40)
            
            dispositivos_zona.append({
                'nombre': d['nombre'],
                'categoria': cat_map.get(d['categoria_id'], 'Sin categoría'),
                'consumo_kwh': consumo,
                'carga_peligrosa': es_peligrosa
            })

    # CA-05: ALERTA cuando consumo_total > limite_kwh, si no NORMAL
    estado_zona = 'ALERTA' if consumo_total > float(zona['limite_kwh']) else 'NORMAL'

    contexto = {
        'zona': zona,
        'dispositivos': dispositivos_zona,
        'consumo_total': consumo_total,
        'cant_dispositivos': len(dispositivos_zona),
        'estado_zona': estado_zona
    }

    return render(request, 'dispositivos/detalle_zona.html', contexto)
