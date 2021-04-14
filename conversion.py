import csv

liste_global=[]
liste_precis=[]



with open("donnee.csv",mode="r") as file:
	reader=csv.reader(file)
	for ligne in reader:
		if ligne[2]=="precis":
			liste_precis.append(ligne)
		if ligne[2]=="general":
			liste_global.append(ligne)



