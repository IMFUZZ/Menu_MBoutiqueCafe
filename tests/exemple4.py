#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Exemple 4 : Supprime toutes les zones d'une fenêtre
    Fait par : Daniel-Junior Dubé et Sarah Laflamme
    Date : 10-12-2015
"""
__author__ = 'Daniel-Junior Dubé & Sarah Laflamme'

from modeles_temporaires import *
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

engine = create_engine('sqlite:///..//src//data//database.db', encoding='utf8', convert_unicode=True)
session = sessionmaker(bind=engine)

s = session()

fenetre_repas = s.query(Fenetre).filter(Fenetre.id == 1).one()
json_fenetre = fenetre_repas.serialiser_en_json()
for zone in json_fenetre['zones']:
    zone['id'] = -zone['id']
fenetre_repas.deserialiser_de_json(s, json_fenetre)
s.commit()

# Résultat : Plus aucune zone ne sera associé à la fenêtre dont l'identifiant est 1
