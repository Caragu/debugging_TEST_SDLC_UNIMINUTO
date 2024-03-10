from flask import Flask, request, render_template, redirect, jsonify
import json
import requests

app = Flask(__name__)

# Lista para almacenar las personas y sus países
personas = []

# Función para cargar registros desde el archivo JSON al inicio
def cargar_registros_desde_json():
    try:
        with open('registros.json', 'r') as json_file:
            registros = json.load(json_file)
            return registros
    except FileNotFoundError:
        return []

# Función para obtener la lista de países desde la API
def obtener_paises_desde_api():
    try:
        response = requests.get('https://restcountries.com/v3.1/all')
        if response.status_code == 200:
            data = response.json()
            countries = [country['name']['common'] for country in data]
            return countries
        else:
            # Manejar un error en la respuesta de la API
            return []
    except Exception as e:
        # Manejar cualquier excepción que ocurra durante la solicitud
        return []

# Cargar registros al iniciar la aplicación
personas = cargar_registros_desde_json()

@app.route('/')
def index():
    return render_template('index.html', personas=personas)

@app.route('/registrar', methods=['POST'])
def registrar():
    nombre = request.form.get('nombre').upper()  # Convertir el nombre a mayúsculas
    pais = request.form.get('pais')
    personas.append({'nombre': nombre, 'pais': pais})
    guardar_registros_en_json(personas)
    return redirect('/')

@app.route('/eliminar/<int:index>', methods=['GET'])
def eliminar(index):
    if 0 <= index < len(personas):
        nombre = personas[index]['nombre']
        pais = personas[index]['pais']
        del personas[index]
        guardar_registros_en_json(personas)
    return redirect('/')

@app.route('/modificar/<int:index>', methods=['GET', 'POST'])
def modificar(index):
    if request.method == 'GET':
        if 0 <= index < len(personas):
            persona = personas[index]
            countries = obtener_paises_desde_api()
            return render_template('modificar.html', index=index, persona=persona, countries=countries)
        return redirect('/')
    elif request.method == 'POST':
        if 0 <= index < len(personas):
            nombre = request.form.get('nombre').upper()
            pais = request.form.get('pais')
            personas[index] = {'nombre': nombre, 'pais': pais}
            guardar_registros_en_json(personas)
        return redirect('/')

# Ruta para cargar los registros en formato JSON
@app.route('/personas_json')
def cargar_personas_json():
    return jsonify(personas)

# Función para guardar los registros en un archivo JSON
def guardar_registros_en_json(registros):
    with open('registros.json', 'w') as json_file:
        json.dump(registros, json_file)

if __name__ == '__main__':
    app.run(debug=True)
