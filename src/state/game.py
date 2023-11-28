import pygame

from ..component.color import Color
from ..component.board import Board
from ..component.cell import Cell
from ..component.button import Button

class Game:
    def __init__(self, display, stateManager):
        self.display = display
        self.stateManager = stateManager

    def set_home(self, home):
        self.home = home

    def run(self, events):
        self.display.fill(Color.get('bg'))