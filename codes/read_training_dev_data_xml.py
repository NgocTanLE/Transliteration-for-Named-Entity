# coding: utf-8
#Encodage du fichier en UTF-8

#Import du module nécessaire
from lxml import etree


### 1. Input
#Lecture du fichier et mise en placa dans une variable
# annuaire = etree.parse('NEWS2018_T-EnVi_trn.xml')
#annuaire = etree.parse('NEWS2018_T-EnVi_dev.xml')
annuaire = etree.parse('NEWS2018_T-EnVi_tst.xml')

compteurSource = 0
compteurTarget = 0

cheminAbsolu = "./data/"
# training data
# pathSource = cheminAbsolu + "train.en-vi.en"
# pathCible = cheminAbsolu + "train.en-vi.vi"

# dev data
#pathSource = cheminAbsolu + "dev.en-vi.en"
#pathCible = cheminAbsolu + "dev.en-vi.vi"

# test data
pathSource = cheminAbsolu + "test.en-vi.en"
pathCible = cheminAbsolu + "test.en-vi.vi"


# open files
file_source = open(pathSource, 'w')
file_cible = open(pathCible, 'w')


### 2. Process
#On se place dans chaque lieu de l'arborescence contenant la balise personne
for noeuds in annuaire.xpath('//TransliterationCorpus/Name'):
        #On récupère l'id
        id = noeuds.get('id')
        for source in noeuds.xpath('SourceName'):
                #Je récupère le nom
                source_recup = source.text
                compteurSource += 1

        #for target in noeuds.xpath('TargetName'):
                #Je récupère le nom
                #target_recup = target.text
                #compteurTarget += 1

### 3. Output

        #J'affiche les résultats
        # print('Source : {}, Target : {}'.format(source_recup, target_recup))
        print(source_recup)
        #print(target_recup)

        # ghi vao trong tap tin tuong ung Source va Target
        file_source.write(source_recup.encode('utf-8') + "\n")
        #file_cible.write(target_recup.encode('utf-8') + "\n")




print('\n\n == Stats == \n\n')
print('#Nombre_elts_Source = ' + str(compteurSource))
#print('#Nombre_elts_Target = ' + str(compteurTarget))


# fermer tous les fichiers
file_source.close()
file_cible.close()

print("\n")
print("*"*80)
print("Fin avec succes")
print("*"*80)
