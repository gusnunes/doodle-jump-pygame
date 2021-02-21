import pygame
from doodler import Doodler
from screen import Screen

class DoodleJumpGame:
    FPS = 30

    def __init__(self):
        pygame.init()

        self.screen  = Screen()
        self.clock   = pygame.time.Clock()
        self.doodler = Doodler(Screen.WIDTH/2, Screen.HEIGHT/2)
    
    def check_border(self):
        if self.doodler.rect.centerx > self.screen.WIDTH:
            self.doodler.rect.centerx = 0
        
        elif self.doodler.rect.centerx < 0:
            self.doodler.rect.centerx = self.screen.WIDTH

    
    def key_pressed(self, key):
        # TODO: colocar WASD para controlar movimento e shoot
        if key[pygame.K_RIGHT]:
            self.doodler.right_movement()

        elif key[pygame.K_LEFT]:
            self.doodler.left_movement()
    
    def run(self):
        while True:
            self.clock.tick(DoodleJumpGame.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.KEYDOWN:   # pressinou e soltou a tecla
                    key = pygame.key.get_pressed()
                    if key[pygame.K_UP] or key[pygame.K_SPACE]:
                        self.doodler.shoot()
                    
            
            self.key_pressed(pygame.key.get_pressed())   # manteve a tecla pressionada
            self.screen.draw_background()
            self.check_border()
            self.screen.draw_doodler(self.doodler.image, self.doodler.rect)
            self.screen.update()
            

def main():
    game = DoodleJumpGame()
    game.run()

if __name__ == "__main__":
    main()
    
