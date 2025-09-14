"""Estelle Doriot
Dessins géomatriques avec turtle
"""

from turtle import *

# carré
for i in range(4):
    forward(40)
    right(90)


clear()


# fonction carré
def carré():
    for i in range(4):
        forward(40)
        right(90)


carré()
clear()


# panneau
def panneau():
    forward(60)
    left(45)
    carré()
    right(45)
    backward(60)


panneau()
clear()


# étoile à 8 branches
def étoile8():
    for i in range(8):
        panneau()
        left(360 / 8)


étoile8()
clear()


# étoile à 11 branches
def étoile11():
    for i in range(11):
        panneau()
        left(360 / 11)


étoile11()
clear()


# étoile quelconque
def étoile(n):
    for i in range(n):
        panneau()
        left(360 / n)


étoile(20)
clear()


# carré de taille quelconque
def carré2(c):
    for i in range(4):
        forward(c)
        right(90)


carré2(20)
clear()


# croix
def branche():
    taille = 100
    for i in range(5):
        carré2(taille)
        forward(taille)
        taille -= 20
    backward(100 + 80 + 60 + 40 + 20)


def croix():
    for i in range(4):
        branche()
        left(90)


croix()
clear()


# triangle
def triangle(c):
    for i in range(3):
        forward(c)
        left(120)


triangle(100)
clear()


# heptagone
def heptagone(c):
    for i in range(7):
        forward(c)
        left(360 / 7)


heptagone(100)
clear()


# polygone
def polygone(n, c):
    for i in range(n):
        forward(c)
        left(360 / n)


polygone(20, 50)
clear()

# ligne de polygones croissants
penup()
goto(-200, 0)
pendown()

for i in range(3, 11):
    polygone(i, 40)
    forward(40)

clear()


# rosace d'octogones
def rosace8(c):
    for i in range(8):
        polygone(8, c)
        right(360 / 8)


rosace8(50)
clear()


# rosace quelconque
def rosace(n, c):
    for i in range(n):
        polygone(n, c)
        right(360 / n)


rosace(20, 30)
clear()


# rosace en couleurs
def rosace_couleurs(n, c):
    couleurs = ["black", "green", "blue", "red", "brown", "purple", "orange", "pink"]
    for i in range(8):
        pencolor(couleurs[i])
        polygone(n, c)
        right(360 / n)


rosace_couleurs(8, 50)
clear()


# rosace en dégradé
def rosace_degrade(n, c):
    d = 0
    for i in range(n):
        pencolor((1 - d, 0, d))
        polygone(n, c)
        right(360 / n)
        d += 1 / n


rosace_degrade(8, 50)
clear()


# rosace pleine
def rosace_pleine(n, c):
    d = 0
    for i in range(n):
        fillcolor((1 - d, 0, d))
        begin_fill()
        polygone(n, c)
        end_fill()
        right(360 / n)
        d += 1 / n


rosace_pleine(8, 50)
clear()


# triangles emboites
def triangles_emboités(c):
    penup()
    goto(-100, -100)
    pendown()
    taille = c
    while taille >= 1:
        triangle(taille)
        forward(taille / 2)
        left(60)
        taille /= 2


triangles_emboités(300)
clear()


# spirale
def spirale():
    d = 0.01
    for i in range(600):
        forward(d)
        right(5)
        d += 0.01


spirale()
clear()


# spirale carrée
def spirale_carre(n):
    taille = 10
    for i in range(n):
        forward(taille)
        right(90)
        taille += 5


spirale_carre(20)
clear()


# spirale polygonale
def spirale_polygone(n, m):
    taille = 10
    for i in range(n):
        forward(taille)
        right(360 / m)
        taille += 5


spirale_polygone(20, 6)
exitonclick()
