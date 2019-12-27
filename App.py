from pygame.locals import *
from random import randint
import pygame
import time
from Game import Game
from Player import Player
from Apple import Apple

class App:

    windowWidth = 800
    windowHeight = 600
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.game = Game()
        self.player = Player(3)
        self.apple = Apple(5,5)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('SNAKE by CANTARIM STUDIOS')
        self._running = True
        self._image_surf = pygame.image.load('snake.png').convert()
        self._apple_surf = pygame.image.load('apple.png')

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
    
    def on_loop(self):
        self.player.update()

        # apple eating logic
        for i in range(0, self.player.length):
            if self.game.isCollision(self.apple.x, self.apple.y, self.player.x[i], self.player.y[i], 32):
             self.apple.x = randint(2,24) * 32
             self.apple.y = randint(2,16) * 32
             self.player.length = self.player.length + 1

        # snake body collision logic
        for i in range(2, self.player.length):
            if self.game.isCollision(self.player.x[0] + 2, self.player.y[0] + 2, self.player.x[i] + 2, self.player.y[i] + 2, 28):
                print('You lose!')
                exit(0)

        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.player.moveRight()

            if (keys[K_LEFT]):
                self.player.moveLeft()

            if (keys[K_UP]):
                self.player.moveUp()

            if (keys[K_DOWN]):
                self.player.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()

            time.sleep(50.0 / 1000.0)
        self.on_cleanup()

if __name__ == '__main__' :
    theApp = App()
    theApp.on_execute()