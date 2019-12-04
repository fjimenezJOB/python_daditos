from pymongo import MongoClient
from flask import session
import  random


MONGO_URL_ATLAS = 'mongodb+srv://franjimenez:Francisco1231998@develop-0hasi.mongodb.net/test?retryWrites=true&w=majority'

client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs = False)

db = client['daditos']

collection_users = db['usuarios']
collection_tiradas = db['tiradas']

def insertar_tiradas(tirada, user):
    collection_tiradas.insert_one({'user': user, 'tiradas': tirada})

def insertar_usuario(user):
    collection_users.insert_one({'user': user})

def sacarRegistro(user):
    tiradas = []
    resultados = collection_tiradas.find({'user'})
    for documento in resultados:
        tiradas.append(documento.get('tiradas'))
    return tiradas

def tirarDados(dados, caras):
    resultado = []
    for i in range(dados):
       dado = random.randint(1, caras)
       resultado.append(dado)
    print(resultado)
    return resultado