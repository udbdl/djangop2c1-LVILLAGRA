# Análisis EcoEnergy - Fase 1

## Relaciones y Claves
El modelo de datos se estructura mediante tres colecciones relacionadas mediante llaves foráneas implícitas[cite: 1]:
* **Zona (1) -> (0..*) Dispositivo:** Se vinculan mediante el campo `zona_id` presente en Dispositivo que apunta a `id` de Zona[cite: 1].
* **Categoria (1) -> (0..*) Dispositivo:** Se vinculan mediante el campo `categoria_id` presente en Dispositivo que apunta a `id` de Categoría[cite: 1].

## Matriz de Criterios de Aceptación
| Criterio | Archivo/Componente | Prueba a realizar |
|---|---|---|
| CA-01 Listado | `views.py / inicio.html` | Cargar `/inicio/` y validar que aparecen los JSON[cite: 1]. |
| CA-02 Tarjeta | `inicio.html` | Visualizar límites y el link al detalle[cite: 1]. |
| CA-03 Detalle | `views.py / catalogo.html`| Entrar a una zona específica y revisar su tabla[cite: 1]. |
| CA-04 Cálculos| `views.py` | Modificar un consumo en JSON y ver cambio en pantalla[cite: 1]. |
| CA-05 Alertas | `views.py / catalogo.html`| Subir consumo para que supere el límite y verificar estado[cite: 1]. |
| CA-06 Escalable| `views.py` | Agregar registros al JSON y recargar página (deben aparecer)[cite: 1].|
| CA-07 Vacío   | `catalogo.html` | Dejar `dispositivos.json` sin registros vinculados a una zona[cite: 1]. |
| CA-08 404     | `views.py` | Entrar a `/catalogo/999/` y recibir error Not Found[cite: 1]. |
| CA-09 - CA-12 | Templates HTML | Achicar navegador y confirmar uso de tablas responsive y colores con texto[cite: 1]. |