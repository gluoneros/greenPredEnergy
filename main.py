from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Diccionario de departamentos y municipios de ejemplo
departamentos_y_municipios = {
'Antioquia': ['Medellín', 
'Abejorral', 
'Abriaquí', 
'Alejandría', 
'Amagá', 
'Amalfi', 
'Andes', 
'Angelópolis', 
'Angostura', 
'Anorí', 
'Anza', 
'Apartadó', 
'Arboletes', 
'Argelia', 
'Armenia', 
'Barbosa', 
'Belén De Bajirá', 
'Bello', 'Belmira', 
'Betania', 
'Betulia', 
'Briceño', 
'Buriticá', 
'Cáceres', 
'Caicedo', 
'Caldas', 
'Campamento', 
'Cañasgordas', 
'Caracolí', 
'Caramanta', 
'Carepa', 
'Carolina', 
'Caucasia', 
'Chigorodó', 
'Cisneros', 
'Ciudad Bolívar', 
'Cocorná', 
'Concepción', 
'Concordia', 
'Copacabana',
'Dabeiba',
'Don Matías',
'Ebéjico',
'El Bagre',
'El Carmen De Viboral',
'El Santuario',
'Entrerrios',
'Envigado',
'Fredonia',
'Frontino',
'Giraldo',
'Girardota',
'Gómez Plata',
'Granada',
'Guadalupe',
'Guarne',
'Guatape',
'Heliconia',
'Hispania',
'Itagüi',
'Ituango',
'Jardín',
'Jericó',
'La Ceja',
'La Estrella',
'La Pintada',
'La Unión',
'Liborina',
'Maceo',
'Marinilla',
'Medellín',
'Montebello',
'Murindó',
'Mutatá',
'Nariño',
'Nechí',
'Necoclí',
'Olaya',
'Peñol',
'Peque',
'Pueblorrico',
'Puerto Berrío',
'Puerto Nare',
'Puerto Triunfo',
'Remedios',
'Retiro',
'Rionegro',
'Sabanalarga',
'Sabaneta',
'Salgar',
'San Andrés',
'San Carlos',
'San Francisco',
'San Jerónimo',
'San José De La Montaña',
'San Juan De Urabá',
'San Luis',
'San Pedro',
'San Pedro De Uraba',
'San Rafael',
'San Roque',
'San Vicente',
'Santa Bárbara',
'Santa Rosa De Osos',
'Santafé De Antioquia',
'Santo Domingo',
'Segovia',
'Sonsón',
'Sopetrán',
'Támesis',
'Tarazá',
'Tarso',
'Titiribí',
'Toledo',
'Turbo',
'Uramita',
'Urrao',
'Valdivia',
'Valparaíso',
'Vegachí',
'Venecia',
'Vigía Del Fuerte',
'Yalí',
'Yarumal',
'Yolombó',
'Yondó',
'Zaragoza',
],
    'Cundinamarca': ['Bogotá', 'Soacha', 'Chía', 'Zipaquirá'],
    'Valle del Cauca': ['Cali', 'Palmira', 'Buenaventura', 'Buga']
}

@app.route('/')
def formulario():
    departamentos = list(departamentos_y_municipios.keys())  # Extrae solo los departamentos
    return render_template('index.html', departamentos=departamentos)

# Ruta para obtener los municipios según el departamento seleccionado

if __name__ == '__main__':
    app.run(debug=True)