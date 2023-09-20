"""



"""
import random

from PIL import Image, ImageDraw


class Cloud:
    def __init__(self, xy):
        self.xy = xy

    def draw(self, ctx):
        ctx.ellipse([(self.xy[0], self.xy[1]), (self.xy[0] + 200, self.xy[1] + 150)], "white")
        ctx.ellipse([(self.xy[0] + 100, self.xy[1] - 40), (self.xy[0] + 380, self.xy[1] + 190)], "white")
        ctx.ellipse([(self.xy[0] + 250, self.xy[1]), (self.xy[0] + 450, self.xy[1] + 170)], "white")


im = Image.open("peppa.png").convert("RGBA")
im_width, im_height = im.size

ctx = ImageDraw.Draw(im)


class Human:
    def __init__(self, ethnie=(255, 255, 255), adult=True, name="John Drip"):

        self.ethnie = ethnie
        self.adult = adult
        if self.adult:
            self.height = 650
            self.width = 350
        else:
            self.height = 400
            self.width = 200
        self.name = name

    def __str__(self):
        return self.name

    def __add__(self, h):

        if self.adult and h.adult:

            r = int((self.ethnie[0] + h.ethnie[0]) / 2)
            g = int((self.ethnie[1] + h.ethnie[1]) / 2)
            b = int((self.ethnie[2] + h.ethnie[2]) / 2)

            return Human((r, g, b), False, name="Caca")
        else:
            return "You can't do this"


    def draw(self):

        x = random.randint(0, im_width - self.width)* 0.85

        # dessin de la tete
        ctx.ellipse([(x + 1 / 6 * self.width, height - self.height),
                     (x + self.width - 1 / 6 * self.width, height - self.height + 1 / 4 * self.height)],
                    self.ethnie)

        # dessin du corps nu
        path = [(x + 1 / 2 * self.width, height - self.height + 1 / 4 * self.height),
                (x + 1 / 2 * self.width, height - self.height + 1 / 4 * self.height + height / 20),  # COU
                (x + self.width, height - 1 / 2 * self.height),  # BRAS DROIT
                (x + 1 / 2 * self.width, height - self.height + 1 / 4 * self.height + height / 20),
                # Retour COU
                (x, height - 1 / 2 * self.height),  # BRAS GAUCHE
                (x + 1 / 2 * self.width, height - self.height + 1 / 4 * self.height + height / 20),
                # Retour COU
                (x + 1 / 2 * self.width, height - 1 / 3 * self.height),  # TRONC
                (x + self.width, height),  # JAMBE DROITE
                (x + 1 / 2 * self.width, height - 1 / 3 * self.height),  # RETOUR TRONC
                (x, height),  # JAMBE GAUCHE
                ]

        # Tracer un trait de couleur de la peau qui relie chaque point du path ci dessus
        for i in range(0, len(path) - 1):
                ctx.line([path[i], path[i + 1]], self.ethnie, 30)


h1 = Human((255, 255, 255), True, "Tulipe")
h2 = Human((100,65,23), True, "Maxime")

h1.draw()
h2.draw()

print(h1)
print(h2)

h3 = h1 + h2
h3.draw()
print(h3)

clouds = [Cloud((random.randint(0, 2000), random.randint(0, 300))),
          Cloud((random.randint(0, 2000), random.randint(0, 300))),
          Cloud((random.randint(0, 2000), random.randint(0, 300))),
          Cloud((random.randint(0, 2000), random.randint(0, 300)))]
for cloud in clouds:
    cloud.draw(ctx)

print(height, width)
im.show()

