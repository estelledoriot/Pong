"""
Contient les éléments du jeu: balle, raquette
"""
from random import choice

import pygame


class Ball(pygame.sprite.Sprite):
    """Gestion de la balle et de ses mouvements
    size: taille de la balle
    position: position initiale de la balle
    """

    def __init__(self, size: int, position: tuple[int, int]) -> None:
        super().__init__()

        # ball
        self.rect: pygame.rect.Rect = pygame.Rect(0, 0, size, size)
        self.rect.center = position
        self.color: pygame.Color = pygame.Color(240, 240, 240)

        # speed
        self.speed_x: int = 7 * choice((-1, 1))
        self.speed_y: int = 7 * choice((-1, 1))

    @property
    def y_position(self) -> int:
        """Hauteur du centre de la balle"""
        return self.rect.centery

    def move(self) -> None:
        """Fait avancer la balle selon sa vitesse"""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def horizontal_bounce(self) -> None:
        """Rebondit sur une surface horizontale"""
        self.speed_y *= -1

    def vertical_bounce(self) -> None:
        """Rebondit sur une surface verticale"""
        self.speed_x *= -1

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
        self.speed_x: int = 7 * choice((-1, 1))
        self.speed_y: int = 7 * choice((-1, 1))

    # TODO faire un rebond sur une raquette qui change la direction de la balle en fonction de la distance au centre de la raquette

    def draw(self) -> None:
        """Dessine la balle à l'écran"""
        fenetre = pygame.display.get_surface()
        pygame.draw.ellipse(fenetre, self.color, self.rect)
