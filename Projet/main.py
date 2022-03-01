import pygame
from game import Game
from player import Player
pygame.init()


# générer la fenêtre de jeu
pygame.display.set_caption("The Spoken Game")
screen = pygame.display.set_mode((1920, 1080))

background = pygame.image.load('assets/background_image.png')

# Charger le jeu
game = Game()

# charger joueur

player = Player()

running = True

while running:

    # Ajout de l'arrière plan
    screen.blit(background, (0, 0))

    # Appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # mettre à jour l'ecran
    pygame.display.flip()

    # Si le joueur ferme la fenêtre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # Detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            # Quelle touche à été utiliser
            if event.key == pygame.K_RIGHT:
                game.player.move_right()
                print("déplacement vers la droit")
            elif event.key == pygame.K_LEFT:
                game.player.move_left()
                print("déplacement vers la gauche")