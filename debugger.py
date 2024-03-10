class Debugger:
    def __init__(self, log_file='debug_log.txt'):
        self.log_file = log_file

    def log(self, message):
        print(message)  # Imprimir el mensaje en la consola
        with open(self.log_file, 'a') as log:
            log.write(message + '\n')  # Guardar el mensaje en el archivo de registro

if __name__ == '__main__':
    debugger = Debugger()

    # Ejemplos de registros de depuración
    debugger.log("Registro de depuración 1")
    debugger.log("Registro de depuración 2")
    debugger.log("Registro de depuración 3")
