import pygame

pygame.init()

text = '水动乐西柚味运动饮料600ml'
font = pygame.font.SysFont('simhei', 40)
ftext = font.render(text, True, (0, 0, 0))
pygame.image.save(ftext, "t.png")

pygame.quit()