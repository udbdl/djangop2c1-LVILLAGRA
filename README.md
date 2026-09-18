# EcoEnergy

Aplicación Django para consultar zonas de consumo energético y los dispositivos instalados en ellas. La información se carga desde `data/zonas.json`, `data/categorias.json` y `data/dispositivos.json`, sin usar Models ni ORM.

## Requisitos

- Python 3.12 o superior
- Django 6.1
- Dependencias de `requirements.txt`

## Instalación y ejecución

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py check
python manage.py runserver
```

macOS/Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
python manage.py check
python manage.py runserver
```

## Rutas funcionales

- `/`: portada EcoEnergy.
- `/zonas/`: listado dinámico de zonas, límite, cantidad de dispositivos y acceso al detalle.
- `/zonas/<id>/`: detalle de una zona, consumo total, categorías, dispositivos y estado `NORMAL` o `ALERTA`.

Una zona sin dispositivos muestra un mensaje informativo. Un identificador inexistente responde con 404.

## Pruebas

```bash
python manage.py test
python -m compileall -q .
```

Las pruebas verifican el listado, el detalle, los estados, una zona sin dispositivos y el 404.
# djangop2c1-LVILLAGRA
