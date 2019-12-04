from pymongo import MongoClient
from flask import session
import  random


MONGO_URL_ATLAS = 'mongodb+srv://franjimenez:Francisco1231998@develop-0hasi.mongodb.net/test?retryWrites=true&w=majority'

client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs = False)

db = client['daditos']

collection_tiradas = db['tiradas']

def insertar_tiradas(tirada, user):
    """
        Inserta las tiradas segun el usuario en la base de datos,
    """
    collection_tiradas.update_one({'user': user}, {'$push': {'tiradas': tirada}})

def insertar_usuario(user):
    """
        Inserta un nuevo usuario si no esta, lo crea, mete los datos en session.
    """
    collection_tiradas.insert_one({'user' :user})

def sacarRegistro(user):
    """
        - Recoje el historial de tiradas de la base de datos por cada usuario.
        - Devuelve una lista de las tiradas que ha realizado.
    """
    tiradas = []
    resultados = collection_tiradas.find({'user': user})

    for documento in resultados:
        tiradas.append(documento.get('tiradas'))
    return tiradas

def tirarDados(dados, caras):
    """
        Devuelve un array con numeros al azar segun el rango de dados y caras por dado.
    """
    resultado = []
    for i in range(dados):
       dado = random.randint(1, caras)
       resultado.append(dado)
    return resultado