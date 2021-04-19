
# A very simple Flask Hello World app for you to get started with...

#! /usr/bin/python
# -*- coding:utf-8 -*-
from donneecours import* #DONC DE LA VARIABLE DICTIONNAIRE
import os
chem=os.getcwd()
from flask import Flask,render_template,send_from_directory,request
app = Flask(__name__,static_folder='static')



@app.route('/service-worker.js')  # UTILISATION DU SERVICE WORKER
def service_worker():

    return app.send_static_file('service-worker.js')

@app.route('/manifesta.json')     #MANIFESTE DE L APPLICATION
def manifest():
    return app.send_static_file('manifesta.json')

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])



@app.route('/')   #AFFICHAGE DU HOME
def accueil():
   # ajout_compteur()
    matiere = ["allemand", "anglais", "russe"]
    return render_template("home.html")




######### MES JEUX ########

@app.route('/jeu')
def jeu():
    ajout_compteur()
    matiere = ["allemand", "anglais", "russe"]
    return render_template("fichier3.html")

@app.route('/jeuAR')
def jeuAR():
    ajout_compteur()
  #  matiere = ["allemand", "anglais", "russe"]
    return render_template("jeuAR.html")

@app.route('/track')
def track():
    return render_template("ar_tracker.html")


    #return render_template('page-2.html')

#####################################




####### SYSTEME DE COURS RUSSE ######

from conversion import *
liste_precis=liste_precis
liste_global=liste_global
print(liste_precis)

@app.route("/precis/")
def control_index_spe():
	liste_nom_lien=[]
	for liste in liste_precis:
		nom=liste[0]
	#	nom=nom.replace(" ","-")
		lien=liste[1]
		liste_nom_lien.append((nom,lien))

	return render_template("templ_menu.html",liste_nom_lien=liste_nom_lien,varlien="precis",categorie="avancé")

@app.route("/general/")
def control_index_glob():
	liste_nom_lien=[]
	for liste in liste_global:
		nom=liste[0]
	#	nom=nom.replace(" ","-")
		lien=liste[1]
		
		liste_nom_lien.append((nom,lien))

	return render_template("templ_menu.html",liste_nom_lien=liste_nom_lien,varlien="general",categorie="débutant")

@app.route("/precis/<nom>") #NOUVEAUTE
def control_frame_spe(nom):
	dict_nom_lien={}
	for liste in liste_precis:
	 
	    nom1=liste[0]
	 #   nom1=nom1.replace(" ","-")
	    lien1=liste[1]
	    dict_nom_lien[nom1]=lien1
	thelien=dict_nom_lien[nom]

	return render_template("templ_frame.html",lien=thelien,nom=nom)

@app.route("/general/<nom>") #NOUVEAUTE
def control_frame_glob(nom):
	dict_nom_lien={}
	for liste in liste_global:
	    nom1=liste[0]
	  #  nom1=nom1.replace(" ","-")
		
	    lien1=liste[1]
	    dict_nom_lien[nom1]=lien1
	thelien=dict_nom_lien[nom]

	return render_template("templ_frame.html",lien=thelien,nom=nom)


####COMPTEUR DE VISITEUR####



############################



#######


#page ERREUR

@app.errorhandler(404)
def ma_page_404(error):
    return "Ma jolie page 404", 404




