import unittest
from app import app
from debugger import Debugger  # Importa la clase Debugger

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.debugger = Debugger(log_file='test_log.txt')  # Crea una instancia de Debugger con un archivo de registro diferente

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.debugger.log("Prueba de página de inicio completada")  # Registro de depuración

    def test_registrar_persona(self):
        response = self.app.post('/registrar', data=dict(nombre='PEDRO_UNIMINUTO', pais='COLOMBIA'))
        self.assertEqual(response.status_code, 302)  # Debe redirigir después de registrar
        self.debugger.log("Prueba de registro de persona completada")  # Registro de depuración

        # Puedes agregar más pruebas aquí, como verificar si los datos se almacenan correctamente en "personas"

if __name__ == '__main__':
    unittest.main()
