# Classe reponsável por controlar o fluxo (e a lógica) do jogo
import pygame
from doodler import Doodler
from screen import Screen
from platform import Platform
import time

class DoodleJumpGame:
    FPS = 30

    def __init__(self):
        pygame.init()

        self.screen  = Screen()
        self.clock   = pygame.time.Clock()
        self.doodler = Doodler(Screen.WIDTH/2, Screen.HEIGHT/2)

        self.p1 = Platform(Screen.WIDTH/2, Screen.HEIGHT/2 + 130)
    
    # jogador aparece do lado oposto ao passar pela borda
    def check_border(self):
        if self.doodler.rect.centerx > self.screen.WIDTH:
            self.doodler.pos_x = 0
        
        elif self.doodler.rect.centerx < 0:
            self.doodler.pos_x = self.screen.WIDTH

    def key_pressed(self, key):
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.doodler.right_movement()

        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            self.doodler.left_movement()
    
    def check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.KEYDOWN:   # pressinou e soltou a tecla
                    key = pygame.key.get_pressed()
                    if key[pygame.K_UP] or key[pygame.K_SPACE] or key[pygame.K_w]:
                        self.doodler.shoot()
        
        self.key_pressed(pygame.key.get_pressed())   # manteve a tecla pressionada
        
    def check_collide(self):
        hits = pygame.sprite.collide_mask(self.doodler,self.p1)
        if hits:
            time.sleep(1)
            self.doodler.pos_y -= self.doodler.SPEED * 20

    def draw(self):
        self.screen.draw_background()
        self.screen.draw_platform(self.p1.image, self.p1.rect)
        self.screen.draw_doodler(self.doodler.image, self.doodler.rect)
        self.screen.update()

    def run(self):
        while True:
            self.clock.tick(DoodleJumpGame.FPS)
            self.check_events()
            self.doodler.update()
            self.draw()
            self.check_collide()
            self.check_border()

def main():
    game = DoodleJumpGame()
    game.run()

if __name__ == "__main__":
    main()
    
