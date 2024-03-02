from ClassForm import Forme
class Trapeze(Forme):
    def __init__(self, Gb=0 , Pb=0 , cote1=0 , cote2=0 , h=0 , x=0 , y=0):
        super().__init__(x, y)
        self.Gb = Gb
        self.Pb = Pb
        self.c0te1 = cote1
        self.cote2 = cote2
        self.h = h

    def saisie(self):
        self.Gb = float(input("entrer la longueur de la grande base : "))
        self.Pb = float(input("entrer la longueur petite base : "))
        self.cote1 = float(input("entrer la longueur du premier  cote : "))
        self.cote2 = float(input("entrer la longueur du deuxieme cote : "))
        self.h = float(input("entrer la hauteur : "))

    def render(self):
        return f"Dimensions du Trapeze : {self.Gb} cm x {self.Pb} cm x {self.cote1} cm x {self.cote2} cm x {self.h} cm"
    
    @property
    def perimetre(self):
        return self.Gb + self.Pb + self.cote1 + self.cote2
    
    @property
    def surface(self):
        return round(((self.Gb + self.Pb)*self.h)/2 , 2)