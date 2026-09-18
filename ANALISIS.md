# Análisis EcoEnergy - Fase 1

## Relaciones y claves

- **Zona (1) -> (0..*) Dispositivo:** `dispositivos.zona_id` referencia `zonas.id`. Una zona puede no tener dispositivos.
- **Categoría (1) -> (0..*) Dispositivo:** `dispositivos.categoria_id` referencia `categorias.id`.
- Los identificadores son únicos dentro de cada archivo JSON y las relaciones se resuelven en Python mediante filtros y un mapa de categorías.

## Componentes principales

- `dispositivos/views.py`: carga JSON, relaciona colecciones, calcula cantidades, consumo y estado, y responde 404.
- `dispositivos/urls.py`: expone `/zonas/` y `/zonas/<id>/`.
- `templates/dispositivos/zonas.html`: listado dinámico de zonas.
- `templates/dispositivos/detalle_zona.html`: métricas, estado y tabla de dispositivos.
- `templates/base.html`: navegación común y Bootstrap.

## Matriz de criterios de aceptación

| Criterio | Archivo/componente | Prueba |
|---|---|---|
| CA-01 | `views.py`, `zonas.html` | Cargar `/zonas/` y comprobar todas las zonas de `zonas.json`. |
| CA-02 | `views.py`, `zonas.html` | Ver nombre, límite, cantidad calculada y enlace al detalle. |
| CA-03 | `views.py`, `detalle_zona.html` | Cargar `/zonas/1/` y comprobar dispositivos, categorías, métricas y estado. |
| CA-04 | `views.py` | Cambiar un consumo válido en JSON y comprobar el nuevo total. |
| CA-05 | `views.py`, `detalle_zona.html` | Comprobar `ALERTA` cuando el total supera el límite y `NORMAL` en caso contrario. |
| CA-06 | `views.py` | Agregar dispositivos válidos al JSON y recargar sin cambiar código. |
| CA-07 | `views.py`, `detalle_zona.html` | Dejar una zona sin dispositivos y comprobar el mensaje informativo. |
| CA-08 | `views.py` | Solicitar `/zonas/999/` y comprobar respuesta 404. |
| CA-09 | `base.html`, templates | Aumentar registros y comprobar navegación y controles accesibles. |
| CA-10 | `detalle_zona.html` | Aumentar columnas o registros y comprobar desplazamiento en `table-responsive`. |
| CA-11 | `base.html`, templates | Revisar jerarquía de navegación, títulos, tarjetas, tabla y mensajes. |
| CA-12 | `detalle_zona.html` | Comprobar que los estados incluyen texto e íconos además del color. |
| CA-13 | `requirements.txt`, README | Instalar dependencias y ejecutar `python manage.py check`. |