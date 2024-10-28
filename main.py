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
        print(data, 'Data')
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
    if request.method == 'POST':
        review = request.form['review']
        print(review)        
        prediction = model.predict([review])
        print(prediction)
        if prediction == 1:
            sentiment = "Positivo"
        elif prediction == 0:
            sentiment = "Negativo"
        else:
            sentiment = "Neutral"
        
        return render_template('index.html', prediction_text=f'El resultado es: {sentiment}')

# Ruta para obtener los municipios según el departamento seleccionado
if __name__ == "__main__":
    app.run(debug=True)
