from unittest.mock import patch

from django.test import TestCase


class EcoEnergyViewsTests(TestCase):
	def test_lista_muestra_zonas_y_cantidad_de_dispositivos(self):
		response = self.client.get("/zonas/")

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Zona Norte - Procesamiento")
		self.assertContains(response, "Dispositivos:")

	def test_detalle_calcula_estado_alerta_y_normal(self):
		alerta = self.client.get("/zonas/2/")
		normal = self.client.get("/zonas/3/")

		self.assertEqual(alerta.status_code, 200)
		self.assertContains(alerta, "ALERTA")
		self.assertContains(normal, "NORMAL")

	def test_zona_sin_dispositivos_muestra_mensaje(self):
		datos = {
			"zonas.json": [{"id": 1, "nombre": "Zona vacía", "limite_kwh": 100}],
			"categorias.json": [],
			"dispositivos.json": [],
		}

		with patch("dispositivos.views.cargar_json", side_effect=lambda nombre: datos[nombre]):
			response = self.client.get("/zonas/1/")

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Esta zona no tiene dispositivos")

	def test_zona_inexistente_responde_404(self):
		response = self.client.get("/zonas/999/")

		self.assertEqual(response.status_code, 404)
