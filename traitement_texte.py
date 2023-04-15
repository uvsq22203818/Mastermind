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
    coor_vert_pt1 = 490-50*(nbr_tentative)
    coor_horiz_pt2 = 40
    coor_vert_pt2 = 460-50*(nbr_tentative)
    for i in range (len(tentative)) :
        plateau.create_oval(coor_horiz_pt1, coor_vert_pt1,\
                            coor_horiz_pt2, coor_vert_pt2, fill=tentative[couleur_cercle])
        coor_horiz_pt1 += 40
        coor_horiz_pt2 += 40
        couleur_cercle += 1

# fonction qui interprète chaques tentatives
def verification():
    if nbr_tentative <= 10 :
        global tentative
        if tentative == combinaison :
            fenetre_victoire = tk.Tk()
            canvas = tk.Canvas(fenetre_victoire, width=300, height=200)
            canvas.grid()
            text = canvas.create_text(150, 50, text="YOU WIN <3 !!!")
        else :
            # ici, on a crée les conditions pour lesquelles
            # on va afficher les cercles qui donnent des indices 
            nb_bienplace= 0
            nb_malplace= 0
            for i in range(taille_code):
                if combinaison[i]==tentative[i]:# on verifie que la couleur est bien placé
                    nb_bienplace+=1 # on compte le nombre de couleur bien placé
                    tentative[i]="x" # on modifie couleur bien placé pour pas qu'elle soit compté plusieurs fois
                else:
                    for j in range(len(tentative)):
                        if combinaison[i]==tentative[j]:# on regarde si les couleurs sont mal placé
                            nb_malplace+=1 # on compte le nombre de couleur mal placé
                            tentative[j]="x" # on modifie couleur mal placé pour pas qu'elle soit compté plusieurs fois
                            break # on sort de la boucle une fois qu'une couleur mal placé ait été compté
                                  # pour une couleur du code
            
            cercle_de_vérif(nb_bienplace, nb_malplace)

            if nbr_tentative==10:
                fenetre_defaite = tk.Tk()
                canvas = tk.Canvas(fenetre_defaite, width=300, height=200)
                canvas.grid()
                text = canvas.create_text(150, 50, text="YOU LOOSE :(")

            print(nb_bienplace)
            print(nb_malplace)
                            
            tentative = []
    

# fonction qui affiche les cercles qui donnent des indices
def cercle_de_vérif(a,b):
    
    coor_horiz_pt1 = 180
    coor_vert_pt1 = 467.5-50*(nbr_tentative-1)
    coor_horiz_pt2 = 195
    coor_vert_pt2 = 482.5-50*(nbr_tentative-1)
    for i in range (a):
        plateau.create_oval(coor_horiz_pt1, coor_vert_pt1,\
                            coor_horiz_pt2, coor_vert_pt2, fill="red")
        coor_horiz_pt1 += 30
        coor_horiz_pt2 += 30

    coor_horiz_pt1 = 180+30*a
    coor_vert_pt1 = 467.5-50*(nbr_tentative-1)
    coor_horiz_pt2 = 195+30*a
    coor_vert_pt2 = 482.5-50*(nbr_tentative-1)
    for i in range (b):
        plateau.create_oval(coor_horiz_pt1, coor_vert_pt1,\
                            coor_horiz_pt2, coor_vert_pt2, fill="white")
        coor_horiz_pt1 += 30
        coor_horiz_pt2 += 30

# def tentative_joueur():
    
    
#     global nbr_tentative
#     nbr_tentative +=1
#     print(tentative)
#     affichage_cercle()
#     verification()

def clic_bouton(color):
    tentative.append(color)
    affichage_cercle()
    if len(tentative)==taille_code:
        global nbr_tentative
        nbr_tentative +=1
        verification()

def clic_rouge():
    clic_bouton("red")        
        
def clic_vert():
    clic_bouton("green") 

def clic_orange():
    clic_bouton("orange") 

def clic_violet():
    clic_bouton("purple")

def clic_bleu():
    clic_bouton("blue") 

def clic_jaune():
    clic_bouton("yellow")        
               
                
               
               
        

# Permet de générer un code aléatoirement
# Fonction appelé par l'utilisation du bouton "1 joueur" dans l'affichage menu
def joueur1_utilise():
    for i in range(taille_code):
        couleur = random.choice(COULEURS)
        combinaison.append(couleur)
    print(combinaison)
    tentative = []
    nbr_tentative= 0
    
# Permet à un deuxième joueur de choisir un code secret.
# Fonction appelé par l'utilisation du bouton "2 joueur" dans l'affichage menu
def joueur2_utilise():
    for i in range (0,4) :
        combinaison.append(input("choisir une couleur (en anglais)"))
    print(combinaison)
    #tentative_joueur()


# programme principal

root = tk.Tk()# création de la fenêtre dans laquelle nous jouerons au "mastermind"
root.title("Mastermind")# titre donné à la fenêtre
root.geometry("400x600")
plateau = tk.Canvas(root,background= "salmon4",width = 300, height = 550)# canvas où s'affichera les pions de couleurs
plateau.grid(row=1, column=1)# positionnement du canvas
# affichage du menu
mode_jeu = tk.Canvas(root, background= "wheat1", width = 300, height= 100)# canvas du "mode de jeu"
mode_jeu.grid(row=0, column=1)# positionnement du canvas

text = mode_jeu.create_text(150, 30, text="Choisissez un mode :")# text qui demande de choisir un mode
bouton1joueur = tk.Button(root, text="1 joueur", command= joueur1_utilise)# bouton pour jouer à 1 joueur
bouton2joueur = tk.Button(root, text="2 joueurs", command= joueur2_utilise)# bouton pour jouer à 2 joueurs
mode_jeu.create_window(100, 70, window=bouton1joueur)# emplacement du bouton "1 joueur"
mode_jeu.create_window(200, 70, window=bouton2joueur)# emplacement du bouton "2 joueurs"
# canvas dans lequel il y a les boutons de couleurs
choix_couleurs = tk.Canvas(root, width= 100, height= 550)
choix_couleurs.grid(row=1, column=0)
# boutons de courleurs:
bouton_red = tk.Button(root, text="rouge", background="red", command= clic_rouge) 
choix_couleurs.create_window(50, 50, window= bouton_red)

bouton_green = tk.Button(root, text="vert", background="green", command= clic_vert) 
choix_couleurs.create_window(50, 100, window= bouton_green)

bouton_blue = tk.Button(root, text="bleu", background="blue", command= clic_bleu) 
choix_couleurs.create_window(50, 150, window= bouton_blue)

bouton_yellow = tk.Button(root, text="jaune", background="yellow", command= clic_jaune) 
choix_couleurs.create_window(50, 200, window= bouton_yellow)

bouton_orange = tk.Button(root, text="orange", background="orange", command= clic_orange) 
choix_couleurs.create_window(50, 250, window= bouton_orange)

bouton_purple = tk.Button(root, text="violet", background="purple", command= clic_violet) 
choix_couleurs.create_window(50, 300, window= bouton_purple)
# affiche le text "Sélectionnez des couleurs:" dans un canvas apparentière
canvas_text2 = tk.Canvas(root, width= 100, height= 100)
canvas_text2.grid(row=0, column=0)
text2 = canvas_text2.create_text(50, 50, text= "Sélectionnez \ndes couleurs :")


root.mainloop()