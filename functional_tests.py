import unittest
from app import app
from debugger import Debugger

#Test de pruebas funcionales
class FunctionalTests(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.debugger = Debugger(log_file='functional_test_log.txt')

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.debugger.log("Prueba funcional: Página de inicio cargada correctamente")

    # Agrega más pruebas funcionales aquí

if __name__ == '__main__':
    unittest.main()
