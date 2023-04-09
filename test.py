import tkinter as tk
nb_tentative=4
tentative=["red","red","red","red"]
rooot = tk.Tk()
#affichage des tentatives
def affichage_cercle():
    
    rooot.geometry("400x800")
    canvas = tk.Canvas(rooot, width=400, height=900)
    couleur_cercle = 0 #prend la couleurs de la tentative
    #variable cercle
    coor_horiz_pt1 = 10
    coor_vert_pt1 = 10+60*(nb_tentative-1)
    coor_horiz_pt2 = 50
    coor_vert_pt2 = 50+60*(nb_tentative-1)
    for i in range (0,4) :
        canvas.create_oval(coor_horiz_pt1, coor_vert_pt1,
                           coor_horiz_pt2, coor_vert_pt2, fill=tentative[couleur_cercle])
        coor_horiz_pt1 += 50
        coor_horiz_pt2 += 50
        couleur_cercle += 1
        canvas.grid()

affichage_cercle()

rooot.mainloop()