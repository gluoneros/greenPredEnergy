from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Diccionario de departamentos y municipios de ejemplo
departamentos_y_municipios = {
    'Antioquia': ['Medellín', 'Envigado', 'Bello', 'Rionegro'],
    'Cundinamarca': ['Bogotá', 'Soacha', 'Chía', 'Zipaquirá'],
    'Valle del Cauca': ['Cali', 'Palmira', 'Buenaventura', 'Buga']
}

@app.route('/')
def formulario():
    departamentos = list(departamentos_y_municipios.keys())  # Extrae solo los departamentos
    return render_template('formulario.html', departamentos=departamentos)

# Ruta para obtener los municipios según el departamento seleccionado
@app.route('/get_municipios', methods=['POST'])
def get_municipios():
    departamento = request.json.get('departamento')
    municipios = departamentos_y_municipios.get(departamento, [])
    return jsonify(municipios)

if __name__ == '__main__':
    app.run(debug=True)