import pygame
w = pygame.display.set_mode((720, 470))
class Sprite():
    image = pygame.image.load('assets/Lizard_front1.png').convert_alpha()


    speed = 5
    x = 100
    y = 100
    def move(self, side):
        if side == "left":
            self.x -= self.speed
        if side == "right":
            self.x += self.speed

time = pygame.time.Clock()
Player = Sprite()

game = True
while game:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        Player.move('right')
    if keys[pygame.K_a]:
        Player.move('left')
    w.fill((0,0,0))
    w.blit(Player.image, (Player.x,Player.y))

    time.tick(30)
    pygame.display.update()
pygame.quit()
