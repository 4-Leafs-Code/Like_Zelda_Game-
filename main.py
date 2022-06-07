import pygame
import sys
from level import Level
from settings import *


class Game:
    def __init__(self):
        """
        The game set up that will initiate the game, the screen, and set the clock.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption("Zelda")
        self.clock = pygame.time.Clock()

        self.level = Level()

        main_sound = pygame.mixer.Sound('audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops = -1)

    def run(self):
        """
        The loop that the game will run inside off and eventually quit from. Also, it fills the screen with a black
        color, updating the screen and controlling the frame rate.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
