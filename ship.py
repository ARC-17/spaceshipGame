import pygame

class Ship():

    def __init__(self, screen):
        """Inicializa a espaçonave e define sua posição inicial."""
        self.screen = screen
        
        self.image = pygame.image.load("..\\spaceshipGame\\images\\nave3.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
       
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        """Desenha a espaçonave em sua posição atual."""
        self.screen.blit(self.image, self.rect)
