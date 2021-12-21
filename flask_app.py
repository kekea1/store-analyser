
# A very simple Flask Hello World app for you to get started with...

#! /usr/bin/python
# -*- coding:utf-8 -*-
import pandas as pd
import play_scraper as ps

from flask import Flask,render_template,request
import time

app = Flask(__name__)



#MOYENNE PRIX OCR
def rm1(text):
  texte=text.replace("+","")
  texte=texte.replace(",","")
  valeur=int(texte)
  return valeur
def rm2(text):
  texte=text.replace("$","")
  valeur=float(texte)
  return valeur



@app.route('/resultat',methods=["GET"])
def hello_world():
    nbpage=request.args.get("page");nbpage=int(nbpage)
    entree=request.args["text"]
    print("AZERRTTYYUIIIHBUYGYU COOOOOOOOOLLLLLLLL")
    recherche=[]
    for nb in range(0,nbpage):
      recherche += ps.search(entree,detailed=True, page=nb)
    
   #     recherche=info+recherche


    dico_base=pd.DataFrame()

    for dico_app in recherche:
        #dico=ps.details(dico_app["app_id"])
        dico={"title":dico_app["title"], "installs":rm1(dico_app["installs"] ),"price":rm2(dico_app["price"]) }
        dico_base=dico_base.append(dico,ignore_index=True)
   # print(dico_base);print(dico_base.columns)

    
    moy2=dico_base["price"].mean()
    moy1=dico_base["installs"].mean()
    quantile25=dico_base["installs"].quantile(.25)
    quantile50=dico_base["installs"].quantile(.50)
    quantile75=dico_base["installs"].quantile(.75)
    html=dico_base.to_html()

    with open("templates/index.html"
, "w") as text_file:
        text_file.write("entree "+entree+"\n")
        text_file.write(html+"\n")
        text_file.write("moyenne_install: "+str(moy1)+"\n")
        text_file.write("moyenne_price: "+str(moy2)+"\n")
        text_file.write("quantile25: "+str(quantile25)+"\n")
        text_file.write("quantile50: "+str(quantile50)+"\n")
        text_file.write("quantile75: "+str(quantile75)+"\n")
    
    time.sleep(2)
    
    
        

    return render_template("index.html")

@app.route('/')
def home():
    return render_template("home.html")



####COMPTEUR DE VISITEUR####



############################



#######


#page ERREUR

@app.errorhandler(404)
def ma_page_404(error):
    return "Ma jolie page 404", 404




