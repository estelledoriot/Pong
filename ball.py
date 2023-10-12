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
        self.screen_width, self.screen_height = pygame.display.get_window_size()

        # ball
        self.rect: pygame.rect.Rect = pygame.Rect(0, 0, size, size)
        self.rect.center = position
        self.color: pygame.Color = pygame.Color(240, 240, 240)

        # speed
        self.speed_x: int = 7 * choice((-1, 1))
        self.speed_y: int = 7 * choice((-1, 1))

    def move(self) -> None:
        """Fait avancer la balle selon sa vitesse"""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    # TODO faire un rebond sur une raquette qui change la direction de la balle en fonction de la distance au centre de la raquette

    def horizontal_bounce(self) -> None:
        """Rebondit sur une surface horizontale"""
        self.speed_y *= -1

    def vertical_bounce(self) -> None:
        """Rebondit sur une surface verticale"""
        self.speed_x *= -1

    def touch_left_border(self) -> bool:
        """Vérifie si la balle touche le bord gauche"""
        return self.rect.left < 0

    def touch_right_border(self) -> bool:
        """Vérifie si le joueur 1 a marqué"""
        return self.rect.right > self.screen_width

    def touch_horizontal_border(self) -> bool:
        """Vérifie si la balle touche un mur horizontal"""
        return self.rect.top < 0 or self.rect.bottom > self.screen_height

    def draw(self, screen: pygame.Surface) -> None:
        """Dessine la balle à l'écran"""
        pygame.draw.ellipse(screen, self.color, self.rect)
