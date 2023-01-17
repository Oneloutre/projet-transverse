import pygame
pygame.init()

pygame.display.set_icon(pygame.image.load("assets/basketball.png"))
pygame.display.set_caption("Basketball Versus", "assets/basketball.png")
pygame.display.set_mode((1080, 720))
running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
            pygame.quit()