import pygame, sys
from .game import Game
from ..component.color import Color
from ..component.button import Button

class Home:
    def __init__(self, display, stateManager, game:Game):
        self.display = display
        self.stateManager = stateManager
        self.font_size = 30
        self.title_text = "Drop the Number"
        self.title_font_size = 60
        self.game = game

        self.hover_play = False
        self.hover_quit = False
        self.button_rect_play = pygame.Rect(0, 0, 200, 50)
        self.button_rect_quit = pygame.Rect(0, 0, 200, 50)

    def draw_title(self):
        title_font = pygame.font.Font(None, self.title_font_size)
        title_surface = title_font.render(self.title_text, True, Color.get('light'))
        title_rect = title_surface.get_rect(center=(self.display.get_width() // 2, self.display.get_height() // 4))
        self.display.blit(title_surface, title_rect)

    def reset(self):
        self.hover_play = False

    def run(self, events):
        self.display.fill(Color.get('bg'))
        self.draw_title()

        Button.draw_dark(self.display, self.button_rect_play, "PLAY", self.hover_play,
                    self.display.get_width() // 2, self.display.get_height() // 2 + 70)
        Button.draw_red(self.display, self.button_rect_quit, "QUIT", self.hover_quit,
                    self.display.get_width() // 2, self.display.get_height() // 2 + 140)

        for event in events:
            if event.type == pygame.MOUSEMOTION:
                self.hover_play = self.button_rect_play.collidepoint(event.pos)
                self.hover_quit = self.button_rect_quit.collidepoint(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.hover_play:
                    self.stateManager.set_state('game')
                if self.hover_quit:
                    pygame.quit()
                    sys.exit()