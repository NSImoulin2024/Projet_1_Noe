"""



"""
from PIL import Image, ImageDraw

"""
class Background:
    def __init__(self, location="street"):
        self.location = location
        self.size = (2000, 1000)
        self.mode = "RGB"




"""



im = Image.new("RGB", (2000, 1000), "skyblue")
width, height = im.size

ctx = ImageDraw.Draw(im)



class Human:
    def __init__(self, taille=1, imc=1, ethnie="yellow"):


        self.ethnie = ethnie
        self.height = [480, 560, 650, 720, 800][taille - 1]
        self.width = [200, 280, 350, 400, 480][imc - 1]
        self.imc = imc

    def draw(self):
        #container (debug)
        #ctx.rectangle([(width/3, height - self.height), (width/3 + self.width, height)], "red")

        #dessin de la tete
        ctx.ellipse([(width/3 + 1/6*self.width, height - self.height), (width/3 + self.width - 1/6*self.width, height - self.height + 1/4*self.height)], self.ethnie)

        #dessin du corps nu
        path = [(width/3 + 1/2*self.width, height - self.height + 1/4*self.height),
                (width/3 + 1/2*self.width, height - self.height + 1/4*self.height + height/20), #COU
                (width/3 + self.width, height - 1/2*self.height), # BRAS DROIT
                (width/3 + 1/2*self.width, height - self.height + 1/4*self.height + height/20), # Retour COU
                (width/3, height - 1/2*self.height), # BRAS GAUCHE
                (width/3 + 1/2*self.width, height - self.height + 1/4*self.height + height/20), # Retour COU
                (width/3 + 1/2*self.width, height - 1/3*self.height), # TRONC
                (width/3 + self.width, height), # JAMBE DROITE
                (width/3 + 1/2*self.width, height - 1/3*self.height), # RETOUR TRONC
                (width/3, height), # JAMBE GAUCHE
                ]

        #Tracer un trait de couleur de la peau qui relie chaque point du path ci dessus
        for i in range(0, len(path) - 1):
            if i == 5:
                ctx.line([path[i], path[i + 1]], self.ethnie, [25, 35, 48, 75, 120][self.imc - 1], "curve")
            else:
                ctx.line([path[i], path[i + 1]], self.ethnie, [20, 30, 40, 50, 60][self.imc - 1])




h = Human(3, 3, "black")
h.draw()

im.show()