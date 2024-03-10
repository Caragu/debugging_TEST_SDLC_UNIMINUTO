import unittest
from app import app
from debugger import Debugger

class UnitTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.debugger = Debugger(log_file='unit_test_log.txt')

    def test_registrar_persona(self):
        response = self.app.post('/registrar', data=dict(nombre='Norberto Caro', pais='Colombia'))
        self.assertEqual(response.status_code, 302)
        self.debugger.log("Prueba unitaria: Registro de persona completado - 1")

    # Agrega más pruebas unitarias aquí

if __name__ == '__main__':
    unittest.main()
