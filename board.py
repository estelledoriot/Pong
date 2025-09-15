"""
classe Board
"""

from enum import Enum

import pygame

Position = Enum("Position", ["GAUCHE", "DROITE"])


class Board(pygame.sprite.Sprite):
    """Gestion des raquettes
    position: droite ou gauche
    color: couleur de la raquette
    up_key, down_key: touches du clavier qui contrôlent les mouvements
    """

    def __init__(
        self,
        position: Position,
        color: pygame.Color,
        up_key: int,
        down_key: int,
    ) -> None:
        super().__init__()

        # dimensions
        self.screen_width, self.screen_height = (
            pygame.display.get_window_size()
        )
        board_width, board_height = 20, 150
        gap = 50

        # board
        self.rect = pygame.Rect(0, 0, board_width, board_height)
        if position == Position.GAUCHE:
            self.rect.midleft = gap, self.screen_height // 2
        if position == Position.DROITE:
            self.rect.midright = (
                self.screen_width - gap,
                self.screen_height // 2,
            )
        self.color: pygame.Color = color

        # speed
        self.speed: int = 10

        # keys
        self.up_key: int = up_key
        self.down_key: int = down_key

    def update(self) -> None:
        """Déplacement de la raquette"""
        # déplacements
        pressed = pygame.key.get_pressed()
        if pressed[self.up_key]:
            self.rect.y -= self.speed
        elif pressed[self.down_key]:
            self.rect.y += self.speed

        # la raquette ne doit pas sortir des limites de la fenêtre
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height

    def draw(self, screen: pygame.Surface) -> None:
        """Dessine la raquette"""
        pygame.draw.rect(screen, self.color, self.rect)
