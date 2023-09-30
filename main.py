"""Ce module utlise la bibliothèque Pillow pour permettre de dessiner des Nuages ainsi que des personnages humanoïdes
personnalisables sur une image de fond

Il contient deux classes: Nuage et Humain, avec leurs méthodes
"""
import random
from PIL import Image, ImageDraw

im = Image.open("background.png").convert("RGBA")
im_width, im_height = im.size
ctx = ImageDraw.Draw(Image.open("background.png").convert("RGBA"))


class Nuage:
    """
        Renvoie un Nuage lié à un contexte graphique
    """

    def __init__(self, context):
        """
        Args:
            context (ImageDraw): Le contexte graphique auquel associer le nuage

        Returns:
            Nuage: Objet Nuage
        """
        self.context = context
        self.xy = (random.randint(0, 2000), random.randint(0, 300))

    def draw(self):
        """
        Dessine le nuage sur son contexte graphique
        Ne prend rien an argument et ne renvoie rien
        """
        self.context.ellipse([(self.xy[0], self.xy[1]), (self.xy[0] + 200, self.xy[1] + 150)], "white")
        self.context.ellipse([(self.xy[0] + 100, self.xy[1] - 40), (self.xy[0] + 380, self.xy[1] + 190)], "white")
        self.context.ellipse([(self.xy[0] + 250, self.xy[1]), (self.xy[0] + 450, self.xy[1] + 170)], "white")


class Humain:
    """
    Renvoie un personnage Humainoïde doté de charactéristiques données
    """
    def __init__(self, context, ethnie="white", adult=True, name="John Doe"):
        """
        Params:
            context (ImageDraw): Le contexte graphique auquel associer le personnage
            ethnie (string | tuple): Choix de l'ethnie du personnage
            adult (bool): Définir le personnage en adulte ou non
            name (string): Nom du personnage

        Returns:
            Humain: Objet Humain

        >>> print(Humain(ctx, "black", True, "Patrick"))
        Patrick
        >>> Humain(ctx, "white", True, "Jean").ethnie
        (255, 255, 255)
        """
        self.context = context

        ethnies = {
            "white": (255, 255, 255),
            "black": (92, 64, 51),
            "latino": (255, 140, 0),
            "asian": (255, 255, 224),
        }

        if type(ethnie) == str:
            self.ethnie = ethnies[ethnie]
        else:
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
        """
        Renvoie le prénom du personnage

        Returns:
              string: Prénom
        """
        return self.name

    def __add__(self, h):
        """
        Renvoie un objet Humain, enfant des deux parents additionnés
        mixé des prénoms des parents

        Args:
            h (Humain): Humain qui va s'additionner

        Returns:
            Humain: Enfant des deux parents

        >>> print(Humain(ctx, "white", True, "John") + Humain(ctx, "black", True, "Alexia"))
        Joxia
        >>> print(Humain(ctx, "asian", True, "John") + Humain(ctx, "asian", False, "Alexia"))
        L'addition n'est pas possible
        """
        if self.adult and h.adult:

            r = (self.ethnie[0] + h.ethnie[0]) // 2
            g = (self.ethnie[1] + h.ethnie[1]) // 2
            b = (self.ethnie[2] + h.ethnie[2]) // 2

            merge = self.name[:len(self.name) // 2] + h.name[len(h.name) // 2:]

            return Humain(self.context, (r, g, b), False, merge)
        else:
            return "L'addition n'est pas possible"

    def draw(self):
        """
        Dessine le personnage sur son contexte graphique
        Ne prend rien an argument et ne renvoie rien
        """
        x = random.randint(0, im_width - self.width) * 0.85

        # dessin de la tete
        self.context.ellipse([(x + 1 / 6 * self.width, im_height - self.height),
                          (x + self.width - 1 / 6 * self.width, im_height - self.height + 1 / 4 * self.height)],
                         self.ethnie)

        # dessin du corps
        path = [(x + 1 / 2 * self.width, im_height - self.height + 1 / 4 * self.height),
                (x + 1 / 2 * self.width, im_height - self.height + 1 / 4 * self.height + im_height / 20),  # COU
                (x + self.width, im_height - 1 / 2 * self.height),  # BRAS DROIT
                (x + 1 / 2 * self.width, im_height - self.height + 1 / 4 * self.height + im_height / 20),  # Retour COU
                (x, im_height - 1 / 2 * self.height),  # BRAS GAUCHE
                (x + 1 / 2 * self.width, im_height - self.height + 1 / 4 * self.height + im_height / 20),  # Retour COU
                (x + 1 / 2 * self.width, im_height - 1 / 3 * self.height),  # TRONC
                (x + self.width, im_height),  # JAMBE DROITE
                (x + 1 / 2 * self.width, im_height - 1 / 3 * self.height),  # RETOUR TRONC
                (x, im_height),  # JAMBE GAUCHE
                ]

        # Trace un trait de couleur de la peau qui relie chaque point du path défini juste au dessus
        for i in range(0, len(path) - 1):
            self.context.line([path[i], path[i + 1]], self.ethnie, 30)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    im = Image.open("background.png").convert("RGBA")
    ctx = ImageDraw.Draw(im)

    h1 = Humain(ctx, "black", True, "Jean")
    h2 = Humain(ctx, "latino", True, "Francois")
    h3 = h1 + h2

    h1.draw()
    h2.draw()
    h3.draw()

    print(h1, h2, h3)

    for i in range(4):
        Nuage(ctx).draw()

    im.show()
