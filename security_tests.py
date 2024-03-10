import unittest
from app import app
from debugger import Debugger

class SecurityTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.debugger = Debugger(log_file='security_test_log.txt')

    def test_seguridad(self):
        # Ejemplo de prueba de seguridad: verifica el acceso no autorizado aquí
        response = self.app.get('/admin')  # Asegúrate de que /admin esté protegido
        self.assertEqual(response.status_code, 404)
        self.debugger.log("Prueba de seguridad: Intento de acceso no autorizado a '/admin'")

if __name__ == '__main__':
    unittest.main()
