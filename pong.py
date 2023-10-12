"""Jeu de Pong (1 ou 2 joueurs)
Il faut rattrapper la balle avec la raquette
"""

import pygame

from ball import Ball
from board import Board, Position
from score import ScoreBoard

# TODO Ajouter le menu pour choisir de jouer à 1 ou 2 joueurs
# TODO Améliorer le mouvement de la raquette automatique
# TODO Corriger le bug de la balle coincée
# TODO Ajouter un timer
# TODO Ajouter une fin du jeu


class Pong:
    """gestion du jeu de Pong"""

    def __init__(self) -> None:
        pygame.init()

        self.largeur: int = 1280
        self.hauteur: int = 900
        self.fenetre: pygame.Surface = pygame.display.set_mode(
            (self.largeur, self.hauteur)
        )
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()

        self.balle: Ball = Ball(30, (self.largeur // 2, self.hauteur // 2))
        self.raquette_gauche: Board = Board(
            Position.GAUCHE, pygame.Color(0, 0, 255), pygame.K_a, pygame.K_q
        )
        self.raquette_droite: Board = Board(
            Position.DROITE, pygame.Color(255, 0, 0), pygame.K_p, pygame.K_m
        )

        self.scores: ScoreBoard = ScoreBoard()

    def tour(self) -> None:
        """Un tour du jeu"""
        # mouvements des raquettes
        self.raquette_gauche.update()
        self.raquette_droite.update()

        # mouvement de la balle
        self.balle.move()

        # rebond sur un mur
        if self.balle.touch_horizontal_border():
            self.balle.horizontal_bounce()

        # point gagné
        if self.balle.touch_left_border():
            self.scores.point_joueur_droit()
            self.balle = Ball(30, (self.largeur // 2, self.hauteur // 2))
        if self.balle.touch_right_border():
            self.scores.point_joueur_gauche()
            self.balle = Ball(30, (self.largeur // 2, self.hauteur // 2))

        # rebond sur une raquette
        if pygame.sprite.collide_rect(
            self.balle, self.raquette_gauche
        ) or pygame.sprite.collide_rect(self.balle, self.raquette_droite):
            self.balle.vertical_bounce()

    def affichage(self) -> None:
        """Affichage des éléments du jeu de Pong"""
        blanc = pygame.Color(255, 255, 255)
        noir = pygame.Color(0, 0, 0)
        # décors
        self.fenetre.fill(noir)
        pygame.draw.line(
            self.fenetre,
            blanc,
            (self.largeur // 2, 0),
            (self.largeur // 2, self.hauteur),
            2,
        )
        pygame.draw.circle(
            self.fenetre, blanc, (self.largeur // 2, self.hauteur // 2), 80, 2
        )
        self.raquette_gauche.draw(self.fenetre)
        self.raquette_droite.draw(self.fenetre)
        self.balle.draw(self.fenetre)
        self.scores.draw()

    def jouer(self) -> None:
        """Lance le jeu"""
        while True:
            self.tour()

            # quitter
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    return

            self.affichage()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    jeu = Pong()
    jeu.jouer()
    pygame.quit()
