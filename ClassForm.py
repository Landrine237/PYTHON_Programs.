from abc import abstractclassmethod
class Forme:
    def __init__(self , x=0 , y=0):
        self.x = x
        self.y = y

@abstractclassmethod
def saisie(self):
    pass

@abstractclassmethod
def render(self):
    pass

@abstractclassmethod
def perimetre(self):
    pass

@abstractclassmethod
def surface(self):
    pass