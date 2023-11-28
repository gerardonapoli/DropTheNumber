import sys
import pygame

from .state.home import Home
from .state.game import Game
from .utilis.stateManager import StateManager

# Initial Setup
CAPTION = "Drop The Number"
WIDTH = 650
HEIGHT = 600
FPS = 30

class DropTheNumber:
    def start():
        pygame.init()
        pygame.display.set_caption(CAPTION)

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()

        stateManager = StateManager('home')
        game = Game(screen, stateManager)
        home = Home(screen, stateManager, game)
        states = {
            'home': home,
            'game': game
        }
        game.set_home(home)
        
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            states[stateManager.get_state()].run(events)

            pygame.display.update()
            pygame.display.flip()
            clock.tick(FPS)