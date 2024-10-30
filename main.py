from flask import Flask, json, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

with open("modelo_test.pkl", "rb") as f:
    model = pickle.load(f)

# Diccionario de departamentos y municipios
with open("localities.json") as loc:
    DEPARTAMENTOS_MUNICIPIOS = json.load(loc)


@app.route("/")
def formulario():
    departamentos = list(
        DEPARTAMENTOS_MUNICIPIOS.keys()
    )  # Extrae solo los departamentos
    return render_template("index.html", departamentos=departamentos)


@app.route("/get_municipios", methods=["POST"])
def get_municipios():
    try:
        # Recibe el JSON enviado desde el cliente
        data = request.get_json()
        departamento = data.get("departamento")
        # Recupera los municipios
        municipios = list(DEPARTAMENTOS_MUNICIPIOS[departamento])
        return jsonify({"municipios": municipios}), 200

    except Exception as e:
        # Log del error
        print(f"Error: {e}")
        return jsonify({"error": "Error al obtener los municipios"}), 500


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # municipio = request.form["municipio"]
        # print(municipio, "<--- municipio")
        # prediction = model.predict([municipio])
        data = request.get_json()
        municipio = data.get("municipio")
        energia_activa = data.get("energia_activa")
        energia_activa = float(energia_activa)
        
        energia_reactiva = data.get("energia_reactiva")
        energia_reactiva = float(energia_reactiva)
        
        dias_lluvia = data.get("dias_lluvia")
        dias_lluvia = float(dias_lluvia)
        
        velocidad_viento = data.get("velocidad_viento")
        velocidad_viento = float(velocidad_viento)
        
        # 'energia_activa', 'energia_reactiva', 'dias_lluvia', 'velocidad_viento'
        # 990127.458333,    272152.864684,      200.60,        1.600000          --> 0
        # 990127.458333,    272152.864684,      149.60,        0.500000          --> 1
        # prediction = model.predict([[990127.458333, 272152.864684, 149.60, 0.500000]])
        prediction = int(model.predict([[energia_activa, energia_reactiva, dias_lluvia, velocidad_viento]])[0])
        # print('VIABLE '+municipio) if prediction == 1 else print(municipio+' NO VIABLE')
        
        justification = ""
        if prediction == 1:
            justification = f"El municipio {municipio} es viable para proyectos de energía renovable."
            if dias_lluvia < 150:
                justification += "Se recomienda un proyecto de energía Solar debido a que llueve menos de 150 días al año."
            elif velocidad_viento > 3.5:
                justification += "Se recomienda un proyecto de energía Eólica debido a que la velocidad promedio del viento es superior al 3.5 m/s."
            elif velocidad_viento > 3.5 and dias_lluvia < 150:
                justification += "Los proyectos de energía Solar y Eólico son ideales por condiciones climáticas ideales."
        else:
            justification = f"El municipio {municipio} NO es viable para proyectos de energía renovable."
            if dias_lluvia > 150 or velocidad_viento < 3.5:
                justification += "No se recomienda un proyecto de energía Eólica debido a que no existen buenas condiciones climáticas."

        # return justification
        return jsonify({"justification": justification, "prediction": False if prediction == 0 else True}), 200

    except Exception as e:
        # Log del error
        print(f"Error: {e}")
        return jsonify({"error": "Error al obtener los municipios"}), 500


# Ruta para obtener los municipios según el departamento seleccionado
if __name__ == "__main__":
    app.run()
