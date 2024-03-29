from PIL import Image, ImageTk
from Constants import e, l
from Enumerations import Status, Action
from labyrinthe.Gomme import Gomme


"""
La classe PacMan. Elle permet de déplacer le héros, manger les gommes, les fantomes si il a mangé
une super gomme...
"""
class PacMan:
    def __init__(self, background, statusPartie, cases):
        self.background = background
        self.statusPartie = statusPartie
        self.cases = cases
        self.x = 0
        self.y = 0
        pacmanImg = Image.open("images/pacman.jpg").resize((int(l / 2), int(l / 2)), resample=0)
        pacmanImg = ImageTk.PhotoImage(pacmanImg)
        self.image = pacmanImg
        self.action = Action.monter
        self.sprite = self.background.create_image(self.x * l + (3 * e), self.y * l + (3 * e), image=self.image)
        self.nb_gomme = 99
        self.ticks = 0
        self.hasMoved = 0

    def monter(self, event):
        if self.statusPartie.get() != Status.enCours.value or self.hasMoved == 2:
            return False
        self.action = Action.monter
        #self.deplacer()

    def descendre(self, event):
        if self.statusPartie.get() != Status.enCours.value or self.hasMoved == 2:
            return False
        self.action = Action.descendre
        #self.deplacer()

    def droite(self, event):
        if self.statusPartie.get() != Status.enCours.value or self.hasMoved == 2:
            return False
        self.action = Action.droite
        #self.deplacer()

    def gauche(self, event):
        if self.statusPartie.get() != Status.enCours.value or self.hasMoved == 2:
            return False
        self.action = Action.gauche
        #self.deplacer()

    def deplacer(self):
        if self.action == Action.monter and not self.cases[self.x][self.y].haut:
            self.y -= 1
            self.hasMoved += 1
        if self.action == Action.descendre and not self.cases[self.x][self.y].bas:
            self.y += 1
            self.hasMoved += 1
        if self.action == Action.droite and not self.cases[self.x][self.y].droite:
            self.x += 1
            self.hasMoved += 1
        if self.action == Action.gauche and not self.cases[self.x][self.y].gauche:
            self.x -= 1
            self.hasMoved += 1
        self.background.coords(self.sprite, self.x * l + (3 * e), self.y * l + (3 * e))
        if self.cases[self.x][self.y].gomme in [Gomme.gomme, Gomme.superGomme]:
            if self.cases[self.x][self.y].gomme == Gomme.superGomme:
                self.ticks = 10
            self.cases[self.x][self.y].gomme = Gomme.vide
            self.background.delete(self.cases[self.x][self.y].sprite)
            self.nb_gomme -= 1
            if self.nb_gomme == 0:
                self.statusPartie.set(Status.gagne.value)

    def mourrir(self):
        self.background.delete(self.sprite)
        self.statusPartie.set(Status.perdu.value)