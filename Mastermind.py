import tkinter as tk
import random
from json import *



# variables
COULEURS = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'hot pink', 'cyan']
taille_code = 4
essais_max = 10
combinaison = []
tentative_courante = [] # tentative
nbr_tentative = 0
liste_rond = [] # liste dans laquelle sera ajouté les ronds de couleurs
liste_tentative = [] # liste dans laquelle sera ajouté les tentatives de la partie


def supprimer_ronds_tentative_courante():
    global liste_rond
    for i in range(len(tentative_courante)):
        rond = liste_rond.pop()
        plateau.delete(rond)

def supprimer_ronds_tentative_derniere():
    global liste_rond
    dernière_tentative = liste_tentative[len(liste_tentative)-1]
    nb_ronds= 4+dernière_tentative["nb_bienplace"]+dernière_tentative["nb_malplace"]
    for i in range(nb_ronds):
        rond = liste_rond.pop()
        plateau.delete(rond)
    
def retour():
    global nbr_tentative
    global tentative_courante
    
    if tentative_courante == []:
        if nbr_tentative>0:
            supprimer_ronds_tentative_derniere()
            nbr_tentative-=1

    else:
        supprimer_ronds_tentative_courante()
        tentative_courante = []  
    
#fonction qui supprime tous les ronds de couleurs
def supprimer_ronds():
    global liste_rond
    for rond in liste_rond:
        plateau.delete(rond)
    liste_rond = []

#fonction qui affiche les cercles
def affichage_cercle(tentative, tous):
    
    couleur_cercle = 0 #prend la couleurs de la tentative
    #variable cercle
    coor_horiz_pt1 = 10
    coor_vert_pt1 = 490-50*(nbr_tentative)
    coor_horiz_pt2 = 40
    coor_vert_pt2 = 460-50*(nbr_tentative)
    for i in range (len(tentative)) : # affiche les cercles au fur et à mesure que la tentative se s'agrandit
        if tous == True or i == len(tentative)-1 :
            rond = plateau.create_oval(coor_horiz_pt1, coor_vert_pt1,\
                                coor_horiz_pt2, coor_vert_pt2, fill= tentative[couleur_cercle])# affecte le rond à une variable
            liste_rond.append(rond)
        coor_horiz_pt1 += 40
        coor_horiz_pt2 += 40
        couleur_cercle += 1

# fonction qui interprète chaques tentatives
def verification():
    
    # ici, on a crée les conditions pour lesquelles
    # on va afficher les cercles qui donnent des indices 
    global tentative_courante
    nb_bienplace= 0
    nb_malplace= 0
    copi_combi= combinaison.copy()
    copi_tentative = tentative_courante.copy()
    for i in range(len(combinaison)):
        if combinaison[i]==tentative_courante[i]:# on verifie que la couleur est bien placé
            nb_bienplace+=1 # on compte le nombre de couleur bien placé
            copi_combi[i] = "x" # on modifie couleur bien placé pour pas qu'elle soit compté plusieurs fois
            tentative_courante[i] = "y"
        
    for j in range(len(combinaison)):
        for k in range(len(tentative_courante)):
            if copi_combi[j] == tentative_courante[k]:# on regarde si les couleurs sont mal placé
                nb_malplace+=1 # on compte le nombre de couleur mal placé
                tentative_courante[k] = "y" # on modifie couleur mal placé pour pas qu'elle soit compté plusieurs fois
                break # on sort de la boucle une fois qu'une couleur mal placé soit compté une seule fois
                      
    

    cercle_de_vérif(nb_bienplace, nb_malplace)
    nouvelle_tentative = { "nb_bienplace": nb_bienplace, "nb_malplace": nb_malplace, "tentative" :copi_tentative}
    liste_tentative.append(nouvelle_tentative)
   
    if nb_bienplace == 4 :
        effacer_message()
        afficher_message("Vous avez gagné !!","20")
        effacer_boutons_couleur()
        afficher_bouton_rejouer()
    elif nbr_tentative==10:
        effacer_message()
        afficher_message("Vous avez perdu :/", "20")
        effacer_boutons_couleur()
        afficher_bouton_rejouer()
    tentative_courante = []
    

# fonction qui affiche les cercles qui donnent des indices
def cercle_de_vérif(a,b):
    
    coor_horiz_pt1 = 180
    coor_vert_pt1 = 467.5-50*(nbr_tentative-1)
    coor_horiz_pt2 = 195
    coor_vert_pt2 = 482.5-50*(nbr_tentative-1)
    for i in range (a):
        rond = plateau.create_oval(coor_horiz_pt1, coor_vert_pt1,\
                            coor_horiz_pt2, coor_vert_pt2, fill="red")
        liste_rond.append(rond)
        coor_horiz_pt1 += 30
        coor_horiz_pt2 += 30

    coor_horiz_pt1 = 180+30*a
    coor_vert_pt1 = 467.5-50*(nbr_tentative-1)
    coor_horiz_pt2 = 195+30*a
    coor_vert_pt2 = 482.5-50*(nbr_tentative-1)
    for i in range (b):
        rond = plateau.create_oval(coor_horiz_pt1, coor_vert_pt1,\
                            coor_horiz_pt2, coor_vert_pt2, fill="white")
        liste_rond.append(rond)
        coor_horiz_pt1 += 30
        coor_horiz_pt2 += 30

   
def clic_bouton(color):
    
    if len(combinaison)<taille_code:
        combinaison.append(color)
        if len(combinaison)==4:
            effacer_message()
            afficher_message("Sélectionnez 4 couleurs\n(jusqu'à trouver le bon code)", "13")
            print(combinaison)
    else:
        tentative_courante.append(color)
        affichage_cercle(tentative_courante,False)
    
    if len(tentative_courante)==taille_code:
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

def clic_rose():
    clic_bouton("hot pink") 

def clic_cyan():
    clic_bouton("cyan")      

def clic_rejouer():
    supprimer_ronds()
    global combinaison
    combinaison = []
    global tentative_courante
    tentative_courante = []
    global nbr_tentative
    nbr_tentative = 0
    afficher_choix_mode()
    effacer_bouton_rejouer()
    effacer_message()
    

def effacer_bouton_rejouer():
    mode_jeu.delete(w_rejouer)
        


def afficher_bouton_rejouer():
    bouton_rejouer = tk.Button(root, text="rejouer", command= clic_rejouer) 
    global w_rejouer
    w_rejouer = mode_jeu.create_window(150, 85, window= bouton_rejouer)

def effacer_boutons_couleur():
    choix_couleurs.delete(w_red)
    choix_couleurs.delete(w_green)
    choix_couleurs.delete(w_orange)
    choix_couleurs.delete(w_purple)
    choix_couleurs.delete(w_blue)
    choix_couleurs.delete(w_yellow)
    choix_couleurs.delete(w_cyan)
    choix_couleurs.delete(w_pink)

def afficher_boutons_couleurs():
    # boutons de courleurs:
    bouton_red = tk.Button(root, text="rouge", background="red", command= clic_rouge) 
    global w_red
    w_red = choix_couleurs.create_window(50, 100, window= bouton_red)

    bouton_green = tk.Button(root, text="vert", background="green", command= clic_vert) 
    global w_green
    w_green= choix_couleurs.create_window(50, 150, window= bouton_green)

    bouton_blue = tk.Button(root, text="bleu", background="blue", command= clic_bleu) 
    global w_blue
    w_blue = choix_couleurs.create_window(50, 200, window= bouton_blue)

    bouton_yellow = tk.Button(root, text="jaune", background="yellow", command= clic_jaune) 
    global w_yellow
    w_yellow = choix_couleurs.create_window(50, 250, window= bouton_yellow)

    bouton_orange = tk.Button(root, text="orange", background="orange", command= clic_orange) 
    global w_orange
    w_orange = choix_couleurs.create_window(50, 300, window= bouton_orange)

    bouton_purple = tk.Button(root, text="violet", background="purple", command= clic_violet) 
    global w_purple
    w_purple = choix_couleurs.create_window(50, 350, window= bouton_purple)

    bouton_pink = tk.Button(root, text="rose", background="hot pink", command= clic_rose) 
    global w_pink
    w_pink = choix_couleurs.create_window(50, 400, window= bouton_pink)

    bouton_cyan = tk.Button(root, text="cyan", background="cyan", command= clic_cyan) 
    global w_cyan
    w_cyan = choix_couleurs.create_window(50, 450, window= bouton_cyan)
    

def effacer_choix_mode():
    mode_jeu.delete(text)
    mode_jeu.delete(w1)
    mode_jeu.delete(w2)

def afficher_choix_mode():
    global text
    text = mode_jeu.create_text(150, 30, text="Choisissez un mode :")# text qui demande de choisir un mode de jeu
    global bouton1joueur
    global bouton2joueur
    bouton1joueur = tk.Button(root, text="1 joueur", command= joueur1_utilise)# bouton pour jouer à 1 joueur
    bouton2joueur = tk.Button(root, text="2 joueurs", command= joueur2_utilise)# bouton pour jouer à 2 joueurs
    
    global w1
    global w2
    w1 = mode_jeu.create_window(100, 70, window=bouton1joueur)# emplacement du bouton "1 joueur"
    w2 = mode_jeu.create_window(200, 70, window=bouton2joueur)# emplacement du bouton "2 joueurs"

def afficher_message(message, taille):
    label_message = tk.Label(root, padx=25, pady=25, text= message,background= "wheat1", font = ("helvetica", taille))
    global w_label_message
    w_label_message = mode_jeu.create_window(150, 50, window= label_message)

def effacer_message():
    mode_jeu.delete(w_label_message)
    

# Permet de générer un code aléatoirement
# Fonction appelé par l'utilisation du bouton "1 joueur" dans l'affichage menu
def joueur1_utilise():
    for i in range(taille_code):
        couleur = random.choice(COULEURS)
        combinaison.append(couleur)
    print(combinaison)
    tentative_courante = []
    nbr_tentative= 0
    effacer_choix_mode()
    afficher_boutons_couleurs()
    afficher_message("Sélectionnez 4 couleurs\n(jusqu'à trouver le bon code)", "13")

# Permet à un deuxième joueur de choisir un code secret.
# Fonction appelé par l'utilisation du bouton "2 joueur" dans l'affichage menu
def joueur2_utilise():
    afficher_message("Composez le code couleur (joueur 2) :", "10")
    effacer_choix_mode()
    afficher_boutons_couleurs()

def sauvegarder():
    fichier = open ("./mastermind.json","w")
    global dic
    dic = {"liste_tentative": liste_tentative, "combinaison": combinaison}
    dump(dic, fichier, indent=4)
    fichier.close()

def restaurer():
    fichier = open ("./mastermind.json","r")
    strjson=fichier.read()
    fichier.close()
    dic = loads(strjson)
    global nbr_tentative
    nbr_tentative = 0
    # restauration de la partie
    for tentative in dic["liste_tentative"]:
        affichage_cercle(tentative["tentative"], True)
        nbr_tentative+=1
        cercle_de_vérif(tentative["nb_bienplace"], tentative["nb_malplace"])
    global combinaison
    combinaison = dic["combinaison"]
    afficher_boutons_couleurs()
    

# programme principal

root = tk.Tk()# création de la fenêtre dans laquelle nous jouerons au "mastermind"
root.title("Mastermind")# titre donné à la fenêtre
root.geometry("400x600+10+10")
plateau = tk.Canvas(root,background= "salmon4",width = 300, height = 550)# canvas où s'affichera les pions de couleurs
plateau.grid(row=1, column=1)# positionnement du canvas
# affichage du menu
mode_jeu = tk.Canvas(root, background= "wheat1", width = 300, height= 100)# canvas du "mode de jeu"
mode_jeu.grid(row=0, column=1)# positionnement du canvas

afficher_choix_mode()

# canvas dans lequel il y a les boutons de couleurs
choix_couleurs = tk.Canvas(root, width= 100, height= 550)
choix_couleurs.grid(row=1, column=0)

# canvas dans lequel il y a les boutons de sauvegarde, restauration, retour en arrière
canvas_fichier = tk.Canvas(root, width = 100, height= 100)
canvas_fichier.grid(row=0, column=0)# positionnement du canvas

# bouton pour sauvegarder
bouton_sauvegarder = tk.Button(root, text="sauvegarder", command= sauvegarder ) 
w_sauvegarder = canvas_fichier.create_window(50, 20, window= bouton_sauvegarder)

# bouton pour restaurer
bouton_restaurer = tk.Button(root, text="restaurer", command= restaurer ) 
w_restaurer = canvas_fichier.create_window(50, 50, window= bouton_restaurer)

# bouton pour revenir en arrière
bouton_retour = tk.Button(root, text="retour", command= retour ) 
w_retour = canvas_fichier.create_window(50, 80, window= bouton_retour)

root.mainloop()