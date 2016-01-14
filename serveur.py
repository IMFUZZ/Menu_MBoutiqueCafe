#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Fichier principal du projet. Définition des routes du serveur.
    Fait par : Daniel-Junior Dubé et Sarah Laflamme
    Date : 10-12-2015
"""

__author__ = 'Daniel-Junior Dubé & Sarah Laflamme'

import json
from bottle import Bottle, error, route, run, request, response, template, static_file, abort, get, post, parse_auth
from os.path import join, dirname, isfile
# from controleur_affichage import *
# from modeles import *

appPath = dirname(__file__) # Représente le chemin vers le répertoire racine du système.
app = Bottle() # Représente l'application qui gère les routes de notre système.

# # DATABASE ENGINE
# engine = create_engine('sqlite:///src//data//database.db', encoding='utf8', convert_unicode=True)
# session = sessionmaker(bind=engine)
# s = session()

# # CONTROLEURS
# c_affichage = ControleurAffichage()

@app.route('/<filename>')
def gestion(filename):
    """
        Fonction associée à une route dynamique qui retourne le 'template' de type 
        'html' s'il existe dans le répertoire '<<appPath>>/src/views'.

        Argument(s) :
            filename (String) : Nom du fichier entrée dans l'URL
    """
    path = join(appPath, 'src', 'views', 'base_gestion.html')
    data = {
        'titre' : filename,
        'path' : path
    }
    print(path)
    return template(join(appPath, 'src', 'views', filename + '.html'), data)

# @app.route('/a/<filename>')
# def affichage(filename):
#     """
#         Fonction associée à une route dynamique qui retourne le 'template' de type 
#         'html' s'il existe dans le répertoire '<<appPath>>/src/views'.

#         Argument(s) :
#             filename (String) : Nom du fichier entrée dans l'URL
#     """
#     menu = c_affichage.generer_json(s, 'fenetre_repas')
#     data = {
#         'titre' : filename,
#         'path' : path,
#         'menu' : menu
#     }
#     return template(join(appPath, 'src', 'views', filename + '.html'), data)

@app.route('/src/<filename:re:.*\.(js|json)>')
def javascripts(filename):
    """
        Fonction associée à une route dynamique qui retourne le fichier statique de type 
        'javascripts' s'il existe dans le répertoire '<<appPath>>/src/js'.

        Argument(s) :
            filename (String) : Nom du fichier entrée dans l'URL
    """
    return static_file(filename, root=join(appPath, 'src', 'js'))

@app.route('/src/<filename:re:.*\.css>')
def stylesheets(filename):
    """
        Fonction associée à une route dynamique qui retourne le fichier statique de type 
        'stylesheets' s'il existe dans le répertoire '<<appPath>>/src/css'.

        Argument(s) :
            filename (String) : Nom du fichier entrée dans l'URL
    """
    return static_file(filename, root=join(appPath, 'src', 'css'))

@app.route('/src/<filename:re:.*\.(jpg|png|gif|ico|jpeg)>')
def images(filename):
    """
        Fonction associée à une route dynamique qui retourne le fichier statique de type 'images' 
        s'il existe dans le répertoire '<<appPath>>/src/images'.

        Argument(s) :
            filename (String) : Nom du fichier entrée dans l'URL
    """
    return static_file(filename, root=join(appPath, 'src', 'images'))

@app.route('/src/<filename:re:.*\.(mp4)>')
def videos(filename):
    """
        Fonction associée à une route dynamique qui retourne le fichier statique de type 'videos' 
        s'il existe dans le répertoire '<<appPath>>/src/videos'.

        Argument(s) :
            filename (String) : Nom du fichier entrée dans l'URL
    """
    return static_file(filename, root=join(appPath, 'src', 'videos'))

@app.route('/src/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    """
        Fonction associée à une route dynamique qui retourne le fichier statique de type 'fonts' 
        s'il existe dans le répertoire '<<appPath>>/src/fonts'.

        Argument(s) :
            filename (String) : Nom du fichier entrée dans l'URL
    """
    return static_file(filename, root=join(appPath, 'src', 'fonts'))
    
@app.route('/')
def main():
    """
        Exemple de route fonctionnelle.
    """
    return "Page d'exemple!"

@app.error(404)
def notFound(error):
    """
        Fonction associée à une route inconnue au système (Erreur 404).

        Argument(s) :
            error (?) : ---
    """
    return 'Erreur 404'

"""
    Lancement de l'application 'app' sur le port '80' de l'hébergeur '0.0.0.0' (localhost) en mode 
    'debug'.
"""
if __name__ == "__main__":
    run(app, host='0.0.0.0', port=80, debug=True)