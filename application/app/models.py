from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

from main import db

class Saludo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    mensaje = db.Column(db.Text, nullable=False)    

    def __repr__(self):
        return f'<Saludo {self.mensaje}>'
 
    @staticmethod
    def get_saludos():
        return Saludo.query.all()

    @staticmethod
    def get_saludo_by_id(id):
        return Saludo.query.filter_by(id=id).all()  
    
    @staticmethod
    def add_saludos(mensaje):
        saludo = Saludo(mensaje=mensaje)
        db.session.add(saludo)
        db.session.commit()

        return {'result':'Saludo registrado correctamente'}

