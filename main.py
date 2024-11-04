import pygame
import random
import json
import os

splash_text = [
    'Some text',
    'Hello world!',
    'Splishy splashy!',
    'much text wow'
]

print('stuff')

config = {
    'title': 'graphic design is my passion',
    'window-width': 800,
    'window-height': 600,
    'background-color': (0, 255, 0),
    'font': 'Comic Sans MS',
    'text-color': (200, 0, 0)
}

if os.path.isfile('config.json'):
    with open('config.json', 'r') as file:
        data = file.read()
        config = json.loads(data)
else:
    with open('config.json', 'w') as file:
        contents = json.dumps(config, indent=4)
        print(contents)
        file.write(contents)



pygame.init()
pygame.display.set_caption(config['title'])
dimensions = (config['window-width'], config['window-height'])
screen = pygame.display.set_mode(dimensions)
pygame.display.get_surface()

pygame.font.init()

font = pygame.font.SysFont('Comic Sans MS', 20)

text_to_display = splash_text[random.randrange(len(splash_text))]
text = font.render(text_to_display, True, (200, 0, 0))

screen_center = (dimensions[0] / 2, dimensions[1] / 2)
text_rect = text.get_rect(center=screen_center)

screen.fill(config['background-color'])
screen.blit(text, text_rect)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False