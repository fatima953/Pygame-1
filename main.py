import pygame

pygame.init()

sw,sh = 500,500

display_surfase = pygame.display.set_mode((sw,sh))

pygame.display.set_caption('Welcome to my game')

bg = pygame.transform.scale(pygame.image.load('bg.png').convert(),(sw,sh))

penguin_image = pygame.transform.scale(pygame.image.load('penguin.png').convert_alpha(),(200,200))

penguin_rect = penguin_image.get_rect(center= (sw //2, sh //2 - 30))

text = pygame.font.font(None, 36).render('HELLO WORLD', True,pygame.color('blue'))

text_rect = text.get_rect(center= (sw //2, sh //2 + 110))

running = True
while running:
    for event in pygame.event.get():
        if event in pygame.type == pygame.Quit:
            running = False
    display_surfase.blit(bg,(0,0))
    display_surfase.blit(penguin_image,penguin_rect)
    display_surfase.blit(text, text_rect)

    pygame.display.flip()
pygame.quit()