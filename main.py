import tkinter

window = tkinter.Tk()

t = 1008
l = 1008/18
h = 504 #l * 9
e = 10

window.title("Pac Man")
window.geometry(str(t)+"x"+str(h))

background = tkinter.Canvas(window, width=t, height=t, background="#000", bd=0, highlightthickness=0)
background.pack()

class Mur:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        background.create_rectangle(x1, y1, x2, y2, fill="#fff", outline="#fff")

class Case:
    # constructeur
    def __init__(self, x: int, y: int, haut: bool, bas: bool, droite: bool, gauche: bool, gum: bool):
        self.x = x # coordonnées case
        self.y = y
        self.haut = haut # murs en haut?
        self.bas = bas
        self.gauche = gauche
        self.droite = droite
        self.gum = gum
        if haut:
            Mur(x*l, y*l, (x+1)*l, y*l+e)
        if bas:
            Mur(x*l, (y+1)*l-e, (x+1)*l, (y+1)*l)
        if gauche:
            Mur(x*l, y*l, x*l+e, (y+1)*l)
        if droite:
            Mur((x+1)*l-e, y*l, (x+1)*l, (y+1)*l)


#Labyrinthe
cases = []
for x in range(0, 18):
    cases.append([])

##ligne 1
cases[0].append(Case(0, 0, True, False, False, True, True))
for x in range(1, 3):
    cases[x].append(Case(x, 0, True, True, False, False, True))
cases[3].append(Case(3, 0, True, False, True, False, True))
cases[4].append(Case(4, 0, False, False, True, True, False))
cases[5].append(Case(5, 0, True, False, False, True, True))
for x in range(6, 12):
    cases[x].append(Case(x, 0, True, True, False, False, True))
cases[12].append(Case(12, 0, True, False, True, False, True))
cases[13].append(Case(13, 0, False, False, True, True, False))
cases[14].append(Case(14, 0, True, False, False, True, True))
for x in range(15, 17):
    cases[x].append(Case(x, 0, True, True, False, False, True))
cases[17].append(Case(17, 0, True, False, True, False, True))
##ligne 2
cases[0].append(Case(0, 1, False, False, True, True, True))
cases[1].append(Case(1, 1, True, False, False, True, False))
cases[2].append(Case(2, 1, True, True, True, False, False))
cases[3].append(Case(3, 1, False, False, True, True, True))
cases[4].append(Case(4, 1, False, True, True, True, False))
cases[5].append(Case(5, 1, False, False, True, True, True))
cases[6].append(Case(6, 1, True, True, False, True, False))
for x in range(7, 11):
    cases[x].append(Case(x, 1, True, True, False, False, False))
cases[11].append(Case(11, 1, True, True, True, False, False))
cases[12].append(Case(12, 1, False, False, True, True, True))
cases[13].append(Case(13, 1, False, True, True, True, False))
cases[14].append(Case(14, 1, False, False, True, True, True))
cases[15].append(Case(15, 1, True, True, False, True, False))
cases[16].append(Case(16, 1, True, False, True, False, False))
cases[17].append(Case(17, 1, False, False, True, True, True))
##ligne 3
cases[0].append(Case(0, 2, False, False, True, True, True))
cases[1].append(Case(1, 2, False, False, True, True, False))
cases[2].append(Case(2, 2, True, False, False, True, True))
for x in range(3, 5):
    cases[x].append(Case(x, 2, False, True, False, False, True))
cases[5].append(Case(5, 2, False, False, False, False, True))
for x in range(6, 8):
    cases[x].append(Case(x, 2, True, True, False, False, True))
for x in range(8, 10):
    cases[x].append(Case(x, 2, True, False, False, False, True))
for x in range(10, 12):
    cases[x].append(Case(x, 2, True, True, False, False, True))
cases[12].append(Case(12, 2, False, False, False, False, True))
for x in range(13, 15):
    cases[x].append(Case(x, 2, False, True, False, False, True))
cases[15].append(Case(15, 2, True, False, True, False, True))
cases[16].append(Case(16, 2, False, False, True, True, False))
cases[17].append(Case(17, 2, False, False, True, True, True))
##ligne4
cases[0].append(Case(0, 3, False, False, True, True, True))
cases[1].append(Case(1, 3, False, True, True, True, False))
cases[2].append(Case(2, 3, False, False, True, True, True))
cases[3].append(Case(3, 3, True, True, False, True, False))
cases[4].append(Case(4, 3, True, True, True, False, False))
cases[5].append(Case(5, 3, False, False, True, True, True))
cases[6].append(Case(6, 3, True, False, False, True, False))
cases[7].append(Case(7, 3, True, True, True, False, False))
cases[8].append(Case(8, 3, False, False, False, True, False))
cases[9].append(Case(9, 3, False, False, True, False, False))
cases[10].append(Case(10, 3, True, True, False, True, False))
cases[11].append(Case(11, 3, True, False, True, False, False))
cases[12].append(Case(12, 3, False, False, True, True, True))
cases[13].append(Case(13, 3, True, True, False, True, False))
cases[14].append(Case(14, 3, True, True, True, False, False))
cases[15].append(Case(15, 3, False, False, True, True, True))
cases[16].append(Case(16, 3, False, True, True, True, False))
cases[17].append(Case(17, 3, False, False, True, True, True))
##ligne5
cases[0].append(Case(0, 4, False, False, False, True, True))
cases[1].append(Case(1, 4, True, True, False, False, True))
cases[2].append(Case(2, 4, False, False, False, False, True))
for x in range(3, 5):
    cases[x].append(Case(x, 4, True, True, False, False, True))
cases[5].append(Case(5, 4, False, False, True, False, True))
cases[6].append(Case(6, 4, False, False, True, True, False))
cases[7].append(Case(7, 4, True, True, False, True, False))
for x in range(8, 10):
    cases[x].append(Case(x, 4, False, True, False, False, False))
cases[10].append(Case(10, 4, True, True, True, False, False))
cases[11].append(Case(11, 4, False, False, True, True, False))
cases[12].append(Case(12, 4, False, False, False, True, True))
for x in range(13, 15):
    cases[x].append(Case(x, 4, True, True, False, False, True))
cases[15].append(Case(15, 4, False, False, False, False, True))
cases[16].append(Case(16, 4, True, True, False, False, True))
cases[17].append(Case(17, 4, False, False, True, False, True))
##ligne6
cases[0].append(Case(0, 5, False, False, True, True, True))
cases[1].append(Case(1, 5, True, False, True, True, False))
cases[2].append(Case(2, 5, False, False, True, True, True))
cases[3].append(Case(3, 5, True, True, False, True, False))
cases[4].append(Case(4, 5, True, True, True, False, False))
cases[5].append(Case(5, 5, False, False, True, True, True))
cases[6].append(Case(6, 5, False, True, False, True, False))
for x in range(7, 11):
    cases[x].append(Case(x, 5, True, True, False, False, False))
cases[11].append(Case(11, 5, False, True, True, False, False))
cases[12].append(Case(12, 5, False, False, True, True, True))
cases[13].append(Case(13, 5, True, True, False, True, False))
cases[14].append(Case(14, 5, True, True, True, False, False))
cases[15].append(Case(15, 5, False, False, True, True, True))
cases[16].append(Case(16, 5, True, False, True, True, False))
cases[17].append(Case(17, 5, False, False, True, True, True))
##ligne 7
cases[0].append(Case(0, 6, False, False, True, True, True))
cases[1].append(Case(1, 6, False, False, True, True, False))
cases[2].append(Case(2, 6, False, True, False, True, True))
for x in range(3, 5):
    cases[x].append(Case(x, 6, True, False, False, False, True))
cases[5].append(Case(5, 6, False, False, False, False, True))
for x in range(6, 12):
    cases[x].append(Case(x, 6, True, True, False, False, True))
cases[12].append(Case(12, 6, False, False, False, False, True))
for x in range(13, 15):
    cases[x].append(Case(x, 6, True, False, False, False, True))
cases[15].append(Case(15, 6, False, True, True, False, True))
cases[16].append(Case(16, 6, False, False, True, True, False))
cases[17].append(Case(17, 6, False, False, True, True, True))
##ligne 8
cases[0].append(Case(0, 7, False, False, True, True, True))
cases[1].append(Case(1, 7, False, True, False, True, False))
cases[2].append(Case(2, 7, True, True, True, False, False))
cases[3].append(Case(3, 7, False, False, True, True, True))
cases[4].append(Case(4, 7, True, False, True, True, False))
cases[5].append(Case(5, 7, False, False, True, True, True))
cases[6].append(Case(6, 7, True, True, False, True, False))
for x in range(7, 11):
    cases[x].append(Case(x, 7, True, True, False, False, False))
cases[11].append(Case(11, 7, True, True, True, False, False))
cases[12].append(Case(12, 7, False, False, True, True, True))
cases[13].append(Case(13, 7, True, False, True, True, False))
cases[14].append(Case(14, 7, False, False, True, True, True))
cases[15].append(Case(15, 7, True, True, False, True, False))
cases[16].append(Case(16, 7, False, True, True, False, False))
cases[17].append(Case(17, 7, False, False, True, True, True))
##ligne 9
cases[0].append(Case(0, 8, False, True, False, True, True))
for x in range(1, 3):
    cases[x].append(Case(x, 8, True, True, False, False, True))
cases[3].append(Case(3, 8, False, True, True, False, True))
cases[4].append(Case(4, 8, False, False, True, True, False))
cases[5].append(Case(5, 8, False, True, False, True, True))
for x in range(6, 12):
    cases[x].append(Case(x, 8, True, True, False, False, True))
cases[12].append(Case(12, 8, False, True, True, False, True))
cases[13].append(Case(13, 8, False, False, True, True, False))
cases[14].append(Case(14, 8, False, True, False, True, True))
for x in range(15, 17):
    cases[x].append(Case(x, 8, True, True, False, False, True))
cases[17].append(Case(17, 8, False, True, True, False, True))


window.mainloop()
