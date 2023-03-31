import tkinter as tk
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 200

# variables
couleurs = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
taille_code = 4
essais_max = 10
tentative = []
combinaison = []
nbr_tentative = 0

root = tk.Tk()
root.title("mastermind")
root.geometry("400x600")
plateau = tk.Canvas(root,background= "salmon4",width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
plateau.grid()



def affichage_cercle():
    #affichage des tentatives
    rooot = tk.Tk()
    rooot.geometry("400x800")
    canvas = tk.Canvas(rooot, width=400, height=900)
    couleur_cercle = 0 #prend la couleurs de la tentative
    #variable cercle
    coor_horiz_pt1 = 10
    coor_vert_pt1 = 10
    coor_horiz_pt2 = 50
    coor_vert_pt2 = 50
    for i in range (0,4) :
        canvas.create_oval(coor_horiz_pt1, coor_vert_pt1, coor_horiz_pt2, coor_vert_pt2, fill=tentative[couleur_cercle])
        coor_horiz_pt1 += 50
        coor_horiz_pt2 += 50
        couleur_cercle += 1
        canvas.grid()


def verification():
    if nbr_tentative <= 10 :
        if tentative == combinaison :
            fenetre_victoire = tk.Tk()
            canvas = tk.Canvas(fenetre_victoire, width=300, height=200)
            canvas.grid()
            text = canvas.create_text(150, 50, text="YOU WIN <3 !!!")
        else :
            tentative_joueur()
    else :
        fenetre_defaite = tk.Tk()
        canvas = tk.Canvas(fenetre_defaite, width=300, height=200)
        canvas.grid()
        text = canvas.create_text(150, 50, text="YOU LOOSE :(")


def tentative_joueur():

    for i in range(0,4):
        tentative.append(input("choisis une couleur parmis : red, green, blue, yellow, orange, purple ---->"))
    global nbr_tentative
    nbr_tentative +=1
    print(tentative)
    verification()
    affichage_cercle()


# Permet de générer un code aléatoirement
# Fonction appelé par l'utilisation du bouton "1 joueur" dans l'affichage menu
def joueur1_utilise():
    for i in range(taille_code):
        couleur = random.choice(couleurs)
        combinaison.append(couleur)
    print(combinaison)
    tentative_joueur()
    return(joueur1_utilise)

# Permet à un deuxième joueur de choisir un code secret.
# Fonction appelé par l'utilisation du bouton "2 joueur" dans l'affichage menu
def joueur2_utilise():
    for i in range (0,4) :
        combinaison.append(input("choisir une couleur (en anglais)"))
    print(combinaison)
    tentative_joueur()


text = plateau.create_text(150, 50, text="choisir un mode")
joueur1 = tk.Button(root, text="1 joueur", command= joueur1_utilise)
joueur2 = tk.Button(root, text="2 joueurs", command= joueur2_utilise)

plateau.create_window(100, 120, window=joueur1)
plateau.create_window(200, 120, window=joueur2)


# def tentative_joueur():
#     tentative = tk.Button(root, text = "saisir une couleur", command =)

root.mainloop()