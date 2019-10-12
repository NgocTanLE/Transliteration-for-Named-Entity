# coding: utf-8
#Encodage du fichier en UTF-8
"""
Auteur: Tan LE
Date de creation: Vendredi 11 Aout 2017
Date de modification: Mardi 08 Mai 2018

Objectif:
	Programme permet de separer en charactere le corpus de training pour NEWS2018 shared task - ACL - Melbourne - Australie
"""

import os   # check the path file


# 1. input
cheminAbsolu = "./" #"/home/letan/Documents/python_exos_LNT/data/transliteration_corpus/"
path = cheminAbsolu + "raw_test.en" 

# 2. process
data = open(path) #.readline() # open text file by tradition
file_result = open(cheminAbsolu + "preprocessed.test.en","w")  # main.en-bn.bn.out

# 3. normalisation by character segmentation
#n=1
for line in data:
    #temp = [line[i:i+n] for i in range(0, len(line), n)]

    temp = list(line)
    #print(temp)
    result = ' '.join(temp)
    print(result)
    file_result.write(str(result))


print("\n")
print("*"*80)

# chemin 
print("Fichier resultat dans le dossier suivant : ")
print(os.path.dirname(os.getcwd()))

data.close()
file_result.close()

print("\n")
print("*"*80)
print("Fin avec succes")
print("*"*80)
