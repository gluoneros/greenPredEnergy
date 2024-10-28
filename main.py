from flask import Flask, json, render_template, request, jsonify
import pickle

app = Flask(__name__)

with open('modelo.pkl', 'rb') as f:
    model = pickle.load(f)

# Diccionario de departamentos y municipios
with open('localities.json') as loc:
    DEPARTAMENTOS_MUNICIPIOS = json.load(loc)

@app.route("/")
def formulario():
    departamentos = list(
        DEPARTAMENTOS_MUNICIPIOS.keys()
    )  # Extrae solo los departamentos
    return render_template("index.html", departamentos=departamentos)

@app.route('/get_municipios', methods=['POST'])
def get_municipios():
    try:
        # Recibe el JSON enviado desde el cliente
        data = request.get_json()
        departamento = data.get('departamento')
        # Recupera los municipios
        municipios = list(
            DEPARTAMENTOS_MUNICIPIOS[departamento]
        )
        return jsonify({"municipios": municipios}), 200

    except Exception as e:
        # Log del error
        print(f"Error: {e}")
        return jsonify({"error": "Error al obtener los municipios"}), 500

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    municipio = data.get('municipio')
    prediction = model.predict([municipio])
    print(prediction, '<--- prediction')
    justify = ""
    if prediction == 1:
        justify = f"El municipio {municipio} es viable para proyectos de energía renovable. "
        # if datos_municipio['dias_lluvia'].values[0] < 150:
        # justify += "Se recomienda un proyecto de energía Solar debido a que llueve menos de 150 al año. "
        # elif datos_municipio['velocidad_viento'].values[0] > 3.5:
        # justify += "Se recomienda un proyecto de energía Eólica debido a que la velocidad promedio del viento es superior al 3.5 m/s."
        # elif datos_municipio['velocidad_viento'].values[0] > 3.5 and datos_municipio['dias_lluvia'].values[0] < 150:
        # justify += "Los proyectos de energía Solar y Eólico son ideales por condiciones climáticas ideales."
    else:
        justify = f"El municipio {municipio} NO es viable para proyectos de energía renovable. "
        # if datos_municipio['dias_lluvia'].values[0] > 150 or datos_municipio['velocidad_viento'].values[0] < 3.5:
        # justify += "No se recomienda un proyecto de energía Eólica debido a que no existen buenas condiciones climáticas. "

    return jsonify({"justify": data}), 200

# Ruta para obtener los municipios según el departamento seleccionado
if __name__ == "__main__":
    app.run(debug=True)
