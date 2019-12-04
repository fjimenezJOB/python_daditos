from pymongo import MongoClient
from flask import session
import random


MONGO_URL_ATLAS = 'mongodb+srv://franjimenez:Francisco1231998@develop-0hasi.mongodb.net/test?retryWrites=true&w=majority'

client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs = False)

db = client['daditos']

collection_users = db['usuarios']
collection_tiradas = db['tiradas']

def insertar_palabra(palabra, tema):
    longitud = len(palabra)
    db.palabras.insert_one({'palabra': palabra, 'tema': tema, 'longitud': longitud})

def borrar_palabras(palabra):
    db.collection_users.delete_one({'palabra': palabra})

def sacarTiradas():
    tiradas = []
    resultados = db.palabras.find()
    
    for documento in resultados:
        tiradas.append(documento.get('tiradas'))
    return tiradas