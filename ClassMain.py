from ClassForm import Forme
from ClassRectangle import Rectangle
from ClassCercle import Cercle
from ClassTrapeze import Trapeze

#if __name__ == "__main__":
#     formes = [Rectangle() , Cercle() , Trapeze()]
#     for forme in formes:
#         forme.saisie()
#         print()

#     for forme in formes:
#         print(forme.render())
#         print("Perimetre  : " , forme.perimetre , "cm carre.")
#         print("Surface" , forme.surface , "cm carre.")
#         print()

class Main():
    def informations(self):
        self.formes = [Rectangle() , Cercle() , Trapeze()]

        for  f in self.formes:
            f.saisie()
            print(f.render())
            print("Perimetre" , f.perimetre , "cm.")
            print("Surface " , f.surface , "cm carre.")
            print()

if __name__ == "__main__":
    main = Main()
    main.informations()

