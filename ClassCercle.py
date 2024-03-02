from ClassForm import Forme
import math
class Cercle(Forme):
    def __init__(self, rayon=0 , x=0 , y=0):
        super().__init__(x, y)
        self.rayon = rayon

    def saisie(self):
        self.rayon = float(input("entrer le rayon du cercle : "))

    def render(self):
        return f"Rayon du Cercle : {self.rayon} cm"
    
    @property
    def perimetre(self):
        return round(2 * math.pi * self.rayon , 2)
    
    @property
    def surface(self):
        return round(math.pi * (self.rayon**2) , 2)