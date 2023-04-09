import tkinter as tk
import random


# variables
COULEURS = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
taille_code = 4
essais_max = 10
combinaison = []
tentative = []
nbr_tentative = 0


def affichage_cercle():
    
    couleur_cercle = 0 #prend la couleurs de la tentative
    #variable cercle
    coor_horiz_pt1 = 10
    coor_vert_pt1 = 10+60*(nbr_tentative-1)
    coor_horiz_pt2 = 50
    coor_vert_pt2 = 50+60*(nbr_tentative-1)
    for i in range (len(tentative)) :
        plateau.create_oval(coor_horiz_pt1, coor_vert_pt1,\
                            coor_horiz_pt2, coor_vert_pt2, fill=tentative[couleur_cercle])
        coor_horiz_pt1 += 50
        coor_horiz_pt2 += 50
        couleur_cercle += 1

# rooot.mainloop()

# fonction qui interprète chaques tentatives
def verification():
    if nbr_tentative <= 10 :
        if tentative == combinaison :
            fenetre_victoire = tk.Tk()
            canvas = tk.Canvas(fenetre_victoire, width=300, height=200)
            canvas.grid()
            text = canvas.create_text(150, 50, text="YOU WIN <3 !!!")
        else :
            # ici, il faudra créer les conditions pour lesquelles
            # on va afficher les cercles qui donnent des indices 
            tentative_joueur()
    else :
        fenetre_defaite = tk.Tk()
        canvas = tk.Canvas(fenetre_defaite, width=300, height=200)
        canvas.grid()
        text = canvas.create_text(150, 50, text="YOU LOOSE :(")

# fonction qui affiche les cercles qui donnent des indices
# def cercle_de_vérif():
#     coor_horiz_pt1 = 10
#     coor_vert_pt1 = 10+60*(nbr_tentative-1)
#     coor_horiz_pt2 = 50
#     coor_vert_pt2 = 50+60*(nbr_tentative-1)
#     for i in range (len(tentative)) :
#         canvas.create_oval(coor_horiz_pt1, coor_vert_pt1, coor_horiz_pt2, coor_vert_pt2, fill=tentative[couleur_cercle])
#         coor_horiz_pt1 += 50
#         coor_horiz_pt2 += 50
#         couleur_cercle += 1
#         canvas.grid()
    


def tentative_joueur():
    tentative = []
    for i in range(0,4):
        tentative.append(input("choisis une couleur parmis : red, green, blue, yellow, orange, purple ---->"))
        global nbr_tentative
        nbr_tentative +=1
    print(tentative)
    affichage_cercle()
    #verification()
    
    


# Permet de générer un code aléatoirement
# Fonction appelé par l'utilisation du bouton "1 joueur" dans l'affichage menu
def joueur1_utilise():
    for i in range(taille_code):
        couleur = random.choice(COULEURS)
        combinaison.append(couleur)
    print(combinaison)
    tentative_joueur()

# Permet à un deuxième joueur de choisir un code secret.
# Fonction appelé par l'utilisation du bouton "2 joueur" dans l'affichage menu
def joueur2_utilise():
    for i in range (0,4) :
        combinaison.append(input("choisir une couleur (en anglais)"))
    print(combinaison)
    tentative_joueur()


# programme principal

root = tk.Tk()
root.title("mastermind")
root.geometry("400x650")
plateau = tk.Canvas(root,background= "salmon4",width = 300, height = 550)
plateau.grid(row=1, column=1)
# affichage du menu
mode_jeu = tk.Canvas(root, background= "wheat1", width = 300, height= 100)
mode_jeu.grid(row=0, column=1)

text = mode_jeu.create_text(150, 30, text="Choisissez un mode :")
bouton1joueur = tk.Button(root, text="1 joueur", command= joueur1_utilise)
bouton2joueur = tk.Button(root, text="2 joueurs", command= joueur2_utilise)
mode_jeu.create_window(100, 70, window=bouton1joueur)
mode_jeu.create_window(200, 70, window=bouton2joueur)
# canvas dans lequel il y a les boutons de couleurs
choix_couleurs = tk.Canvas(root, width= 100, height= 550)
choix_couleurs.grid(row=1, column=0)
# boutons de courleurs:
bouton_red = tk.Button(root, text="red", background="red", command= print("red")) 
choix_couleurs.create_window(50, 50, window= bouton_red)

bouton_green = tk.Button(root, text="green", background="green", command= print("green")) 
choix_couleurs.create_window(50, 100, window= bouton_green)

bouton_blue = tk.Button(root, text="blue", background="blue", command= print("blue")) 
choix_couleurs.create_window(50, 150, window= bouton_blue)

bouton_yellow = tk.Button(root, text="yellow", background="yellow", command= print("yellow")) 
choix_couleurs.create_window(50, 200, window= bouton_yellow)

bouton_orange = tk.Button(root, text="orange", background="orange", command= print("orange")) 
choix_couleurs.create_window(50, 250, window= bouton_orange)

bouton_purple = tk.Button(root, text="purple",background="purple", command= print("purple")) 
choix_couleurs.create_window(50, 300, window= bouton_purple)
# affiche le text "Sélectionnez des couleurs:" dans un canvas apparentière
canvas_text2 = tk.Canvas(root, width= 100, height= 100)
canvas_text2.grid(row=0, column=0)
text2 = canvas_text2.create_text(50, 50, text= "Sélectionnez \ndes couleurs :")


# def tentative_joueur():
#     tentative = tk.Button(root, text = "saisir une couleur", command =)

root.mainloop()