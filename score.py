"""
classe ScoreBoard
"""

import pygame


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
