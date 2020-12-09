
# A very simple Flask Hello World app for you to get started with...

#! /usr/bin/python
# -*- coding:utf-8 -*-
from donneecours import*

from flask import Flask,render_template,send_from_directory,request
app = Flask(__name__,static_folder='static')

#with open("data.txt","w") as f:
#    f.write("0")
######FONCTIONS GLOBALES ######

@app.template_global()
def lire():
    with open("data.txt","r") as fich:
        donnee_fich=fich.read()
    return donnee_fich


@app.template_global()
def ajout_compteur():
    donnee_fich=lire()
  #  print(donnee_fich+"/n")

    with open("data.txt","w") as fich:
        donnee_fich=int(donnee_fich)
        donnee_fich+=1

        fich.write(str(donnee_fich))

################################



for val in elements:
	for minival in val:
		for unite in minival:
			print(unite)

@app.route('/service-worker.js')
def service_worker():

    return app.send_static_file('service-worker.js')

@app.route('/manifesta.json')
def manifest():
    return app.send_static_file('manifesta.json')

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])



@app.route('/')
def accueil():
    ajout_compteur()
    matiere = ["allemand", "anglais", "russe"]
    return render_template("home.html")


@app.route('/page2')
def page2():
    ajout_compteur()
    matiere = ["allemand", "anglais", "russe"]
    #return render_template("/plus/testplus.html")


    return render_template('page-2.html')

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


@app.route("/<lamatiere>/<unite>/souspartie/<numsp>")
def souspartieAng(lamatiere,unite,numsp):
	return render_template("/"+lamatiere+"/"+unite+"/souspartie/"+numsp+".html")


@app.route("/<matiere>/<unite>/")
def control_index(matiere,unite):
	eval("from templates."+matiere+"."+unite+" import *")

	return render_template("template_index_unite.html",parties=parties,nomsparties=nomsparties)


####### SYSTEME DE COURS LATIN ######
from donnee_frame import*


@app.route('/latin/declinaisons/<sujet>')
def accueilpyd(sujet):

    ajout_compteur()

    return render_template("squelette.html",
        leiframe=declinaisons[sujet],
        sujet=sujet)

@app.route('/latin/')
def acceuil_latin():

    ajout_compteur()
    return render_template("menu_latin.html")


####COMPTEUR DE VISITEUR####

@app.route('/compteur')
def main2():

    donnee=lire()
    return donnee

############################



#######


#page ERREUR

@app.errorhandler(404)
def ma_page_404(error):
    return "Ma jolie page 404", 404



if __name__ == '__main__':
    app.run()


