"""
Contient les éléments du jeu: balle, raquette
"""
from random import choice
import pygame


class Balle(pygame.sprite.Sprite):
    """Gestion de la balle et de ses mouvements
    taille: taille de la balle
    """

    def __init__(self, taille: int) -> None:
        super().__init__()

        largeur, hauteur = pygame.display.get_window_size()

        self.rect: pygame.rect.Rect = pygame.Rect(0, 0, taille, taille)
        self.rect.center = largeur // 2, hauteur // 2
        self.vx: int = 7 * choice((-1, 1))
        self.vy: int = 7 * choice((-1, 1))
        self.color: pygame.Color = pygame.Color(240, 240, 240)

    def marque_joueur_droite(self) -> bool:
        """Vérifie si le joueur 2 a marqué"""
        return self.rect.left <= 0

    def marque_joueur_gauche(self) -> bool:
        """Vérifie si le joueur 1 a marqué"""
        largeur, _ = pygame.display.get_window_size()
        return self.rect.right >= largeur

    def touche_murs(self) -> bool:
        """Vérifie si la balle touche un mur horizontal"""
        _, hauteur = pygame.display.get_window_size()
        return self.rect.top <= 0 or self.rect.bottom >= hauteur

    def relance(self) -> None:
        """Relance la balle à partir du milieu"""
        largeur, hauteur = pygame.display.get_window_size()
        self.rect.center = largeur // 2, hauteur // 2
        self.vx: int = 7 * choice((-1, 1))
        self.vy: int = 7 * choice((-1, 1))

    def avance(self) -> None:
        """Fait avancer la balle selon sa vitesse"""
        self.rect.x += self.vx
        self.rect.y += self.vy

    def rebond_horizontal(self) -> None:
        """Rebondit sur une surface horizontale"""
        self.vy *= -1

    def rebond_vertical(self) -> None:
        """Rebondit sur une surface verticale"""
        self.vx *= -1

    # TODO faire un rebond sur une raquette qui change la direction de la balle en fonction de la distance au centre de la raquette

    @property
    def hauteur(self) -> int:
        """Hauteur du centre de la balle"""
        return self.rect.centery

    def draw(self) -> None:
        """Dessine la balle à l'écran"""
        fenetre = pygame.display.get_surface()
        pygame.draw.ellipse(fenetre, self.color, self.rect)


class Raquette(pygame.sprite.Sprite):
    """Gestion des raquettes
    position: droite ou gauche
    couleur: couleur de la raquette
    touche_haut, touche_bas: touches du clavier qui contrôlent les mouvements
    """

    def __init__(
        self, position: str, couleur: pygame.Color, touche_haut: int, touche_bas: int
    ) -> None:
        super().__init__()

        largeur, hauteur = pygame.display.get_window_size()
        largeur_raquette = 20
        hauteur_raquette = 150
        ecart_mur = 20

        self.rect = pygame.Rect(0, 0, largeur_raquette, hauteur_raquette)
        if position == "gauche":
            self.rect.midleft = ecart_mur, hauteur // 2
        else:
            self.rect.midright = largeur - ecart_mur, hauteur // 2

        self.vitesse: int = 10
        self.couleur: pygame.Color = couleur
        self.touche_haut: int = touche_haut
        self.touche_bas: int = touche_bas

    def deplacement(self, balle_y: int) -> None:
        """Déplacement de la raquette"""
        pressed = pygame.key.get_pressed()
        if pressed[self.touche_haut]:
            self.rect.y -= self.vitesse
        elif pressed[self.touche_bas]:
            self.rect.y += self.vitesse

        _, hauteur = pygame.display.get_window_size()
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > hauteur:
            self.rect.bottom = hauteur

    def draw(self) -> None:
        """Dessine la raquette"""
        fenetre = pygame.display.get_surface()
        pygame.draw.rect(fenetre, self.couleur, self.rect)


class RaquetteAutomatique(Raquette):
    """Raquette gérée par l'ordinateur (pour une version 1 joueur)"""

    def deplacement(self, balle_y: int) -> None:
        """Déplacement de la raquette de façon automatique"""
        if balle_y > self.rect.centery:
            self.rect.y += self.vitesse
        elif balle_y < self.rect.centery:
            self.rect.y -= self.vitesse


class ScoreBoard:
    """Gestion des scores des joueurs"""

    def __init__(self) -> None:
        self.score_gauche = 0
        self.score_droit = 0
        self.police: pygame.font.Font = pygame.font.Font("font/homespun.ttf", 30)

        fenetre = pygame.display.get_surface()
        self.surface: pygame.Surface = self.police.render(
            self.texte, True, pygame.Color(240, 240, 240)
        )
        self.rect = self.surface.get_rect(center=(fenetre.get_width() // 2, 50))

    @property
    def texte(self) -> str:
        """Texte des scores à afficher"""
        return f"{self.score_gauche:02d} {self.score_droit:02d}"

    def point_joueur_gauche(self) -> None:
        """Ajoute un point au joueur gauche"""
        self.score_gauche += 1

    def point_joueur_droit(self) -> None:
        """Ajoute un point au joueur droit"""
        self.score_droit += 1

    def draw(self) -> None:
        """Affiche le score"""
        fenetre = pygame.display.get_surface()
        self.surface = self.police.render(self.texte, True, pygame.Color(240, 240, 240))
        fenetre.blit(self.surface, self.rect)
