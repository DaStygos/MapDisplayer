
from geographie import *

directions = ["nordouest","nord","nordest","ouest","milieu","est","sudouest","sud","sudest"]
altitude = []
altitude2 = []
alt = []
a = 0
for i in range(9):
    altitude.append([])
    f = open(directions[i] +".asc")
    listealtitude = f.read()
    listealtitude = listealtitude.split("\n")
    listealtitude = listealtitude[6:]
    for j in range(1000):
        ligne = listealtitude[j]
        ligne = ligne.split(" ")
        ligne.pop(0)
        altitude[i].append(ligne)
for grille in altitude:
    grille2 = [[] for _ in range(333)]
    for i in range(333):
         for j in range(333):
             grille2[i].append(grille[i*3][j*3])
    altitude2.append(grille2)
for i in range(999):
    if i < 333:
        alt.append(altitude2[0][i]+altitude2[1][i]+altitude2[2][i]+[0.0])
    elif i > 332 and i < 666:
        alt.append(altitude2[3][i-333]+altitude2[4][i-333]+altitude2[5][i-333]+[0.0])
    else:
        alt.append(altitude2[6][i-666]+altitude2[7][i-666]+altitude2[8][i-666]+[0.0])
alt.append([0.0 for _ in range(1000)])
direc = "nord"
relief(1000,alt,600,525,direc)

altitude = []
altitude2 = []
alt = []
a = 0
for i in range(9):
    altitude.append([])
    f = open(directions[i] +".asc")
    listealtitude = f.read()
    listealtitude = listealtitude.split("\n")
    listealtitude = listealtitude[6:]
    for j in range(1000):
        ligne = listealtitude[j]
        ligne = ligne.split(" ")
        ligne.pop(0)
        altitude[i].append(ligne)
for grille in altitude:
    grille2 = [[] for _ in range(333)]
    for i in range(333):
         for j in range(333):
             grille2[i].append(grille[i*3][j*3])
    altitude2.append(grille2)
for i in range(999):
    if i < 333:
        alt.append(altitude2[0][i]+altitude2[1][i]+altitude2[2][i]+[0.0])
    elif i > 332 and i < 666:
        alt.append(altitude2[3][i-333]+altitude2[4][i-333]+altitude2[5][i-333]+[0.0])
    else:
        alt.append(altitude2[6][i-666]+altitude2[7][i-666]+altitude2[8][i-666]+[0.0])
alt.append([0.0 for _ in range(1000)])
affichage_carte(1000,alt)