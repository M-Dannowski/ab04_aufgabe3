import os
import pygame

class Settings:
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 800
    FPS = 60
    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(FILE_PATH, "images")


class Defender(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "defender01.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10, 80)
        self.speedx = 5
        self.speedy = 1

    def update(self):
        self.rect = self.rect.move(self.speedx, self.speedy)
        if self.rect.left < 0 or self.rect.right > Settings.WINDOW_WIDTH:
            self.speedx *= -1
        if self.rect.top < 0 or self.rect.bottom > Settings.WINDOW_HEIGHT:
            self.speedy *= -1


class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "alienbig0101.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 45))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10, 10)
        self.speedx = 1
        self.speedy = -5

    def update(self):
        self.rect = self.rect.move(self.speedx, self.speedy)
        if self.rect.left < 0 or self.rect.right > Settings.WINDOW_WIDTH:
            self.speedx *= -1
        if self.rect.top < 0 or self.rect.bottom > Settings.WINDOW_HEIGHT:
            self.speedy *= -1


def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 50"
    pygame.init()

    screen = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
    pygame.display.set_caption("Bitmaps laden und ausgeben")
    clock = pygame.time.Clock()

    defender = Defender()
    alien = Alien()

    background_image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "background03.png")).convert()
    background_image = pygame.transform.scale(background_image, (Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))

    hindernis_image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "hindernis.png")).convert()
    hindernis_image = pygame.transform.scale(hindernis_image, (30,30))


    hindernisse_positionen = [(100, 150),(300, 400),(500, 200),(700, 600),(850, 350)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        alien.update()
        defender.update()

        screen.blit(background_image, (0, 0))
        screen.blit(alien.image, alien.rect)
        screen.blit(defender.image, defender.rect)
        #screen.blit(hindernis_image, hindernisse_positionen)

        pygame.display.flip()
        clock.tick(Settings.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
