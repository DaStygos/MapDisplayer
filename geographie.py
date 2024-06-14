# import des librairies nécessaires


from random import randint
from PIL import Image
from math import *


# définition de la fonction de traitement de la carte


def affichage_carte(taille : int,pixels : list):
    """Réalise une carte de taille définie à partir des pixels

    Paramètres:
        taille : la largeur/longueur de la zone dont on veut la carte
        type(taille) : entier
        pixels : tous les pixels dont on dispose pour faire la carte
        type(pixels) : liste de liste de tuples d'entiers
    Renvoie:
        carte, la carte correspondant aux pixels
        type(carte) : une image affichable avec PIL"""
    carte = Image.new("RGB",(taille,taille))
    for i in range(taille):
        for j in range(taille):
            a = round((float(pixels[i][j])/2000)*255)
            carte.putpixel((j,i),(a,a,a))
    carte.show()
    carte.save("map.png")


# définition des fonctions de ray tracing


def points_sur_ligne(x_depart : int, y_depart : int, angle : float, taille : int) -> list:
    """Trouve les points qui sont coupés par un rayon d'un certain angle

    Paramètres:
        x_depart,y_depart : les coordonnées d'où le rayon part
        angle : l'angle du rayon qu'on veut tester (en radian)
        taille : la largeur/longueur de la grille
    Renvoie:
        resultat, les points qui sont coupés par le rayon"""
    resultat = []
    rayon = taille//20
    x = x_depart
    y = y_depart
    while 0 <= x < taille and 0 <= y < taille :
        resultat.append((x,y))
        rayon += 1
        x = x_depart +round(rayon*cos(angle))
        y = y_depart + round(rayon*sin(angle))
    return resultat


def point_le_plus_haut(ligne : list,altitude : list,colonne : int,x : int,y : int,taille : int) -> list:
    """Trouve le point dont l'altitude forme l'angle le plus élevé

    Paramètres:
        ligne : les points dont on teste l'altitude
        altitude : les données d'altitude
        colonne : le numéro de la colonne correspondante
        x,y : les coordonnées du point a tester
        taille : la taille de la grille
    Renvoie:
        hauteurs, l'angle (en radian) et la distance au point
        type(resultat) : tuple contenant un float et un entier"""
    hauteurs = []
    anglemax = 0
    for point in ligne:
        elevation = float(altitude[point[0]][point[1]])-float(altitude[x][y])
        distance = sqrt((abs(point[0]-x))**2 + (abs(point[1]-y))**2)
        if distance != 0:
            tan = elevation/(25*distance)
            if atan(tan) > anglemax:
                hauteurs.append(((atan(tan)/(pi/4))*taille,colonne))
                anglemax = atan(tan)
            else:
                hauteurs.append((0,colonne))
        else:
            hauteurs.append((0,colonne))
    return (hauteurs)


def liste_plus_hauts(taille :int ,altitude : list,x : int,y : int,orientation) -> list:
    """Trouve les points d'altitude croissante pour chacune des lignes visibles

    Paramètres:
        taille : la taille de la grille
        altitude : les données d'altitude
        x,y : coordonnées du point a tester
        orientation : la direction à regarder
    Renvoie:
        hauteurs, les points les plus hauts de chaque ligne
        type(hauteurs) : liste de tuples"""
    coordonnees = []
    hauteurs = []
    if orientation == "nord":
        a = 3*pi/4
    elif orientation == "sud":
        a = 7*pi/4
    elif orientation == "est":
        a = pi/4
    elif orientation == "ouest":
        a = 5*pi/4
    else:
        a = orientation
    for i in range(taille):
        ligne = points_sur_ligne(x,y,(i/taille)*pi/2+a,taille)
        points = point_le_plus_haut(ligne,altitude,i,x,y,taille)
        for j in points:
            if j[0] != 0:
                hauteurs.append((int(j[0])//3,int(j[1])))
    return hauteurs

def relief(taille : int,altitude : list,x : int,y : int,orientation):
    """Affiche l'image correspondante au relief observable
    
    Paramètres :
        taille : la taille de la grille
        altitude : la grille des altitudes des points
        x,y : coordonnées du point a tester
        orientation : la direction à regarder"""
    hauteurs = liste_plus_hauts(taille,altitude,x,y,orientation)
    cretes = Image.new("1",(taille,taille//3))
    for i in range(len(hauteurs)):
        if 0 <= hauteurs[i][0] < taille and 0 <= hauteurs[i][1] < taille:
            cretes.putpixel((taille-1-hauteurs[i][1],(taille//3-1-hauteurs[i][0])),256)
    cretes.save("image.png")
    cretes.show()