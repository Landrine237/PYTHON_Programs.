from ClassForm import Forme
class Rectangle(Forme):
    def __int__(self , width=0 , height=0 , x=0 , y=0):
        super().__init(x , y)
        self.width = width
        self.height = height

    def saisie(self):
        self.width = float(input("entrer la longueur du rectangle : "))
        self.height = float(input("entrer la largeur du rectangle : "))
    
    def render(self):
        return f"Dimensions du Rectangle : {self.width} cm x {self.height} cm"
    
    @property
    def perimetre(self):
        return round((self.width + self.height)*2 , 2)
    
    @property
    def surface(self):
        return round(self.width * self.height , 2)