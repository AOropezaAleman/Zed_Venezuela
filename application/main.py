from app import create_app, database
from flask import jsonify, request

app = create_app()
db = database()
from app.models import Saludo

@app.route('/saludos')
def get_greeting():
    mensajes = {} 
    if request.args.get('id') is None:
       mensajes = Saludo.get_saludos()
    else:
       mensajes = Saludo.get_saludo_by_id(request.args.get('id'))

       if len(mensajes) == 0:
          return "Registro no encontrado", 400 

    saludos = {'saludos': []}
    for saludo in mensajes:
      saludo_mensaje = {'mensaje': saludo.__dict__['mensaje']}
      saludos['saludos'].append(saludo_mensaje)

    return saludos       

@app.route('/saludos', methods=["POST"])
def add_greeting():
    mensaje = request.json['mensaje']
    return jsonify(Saludo.add_saludos(mensaje))

