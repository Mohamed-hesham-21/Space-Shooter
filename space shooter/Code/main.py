import pygame
import random

pygame.init()

World_Width, World_Height = 1280 , 720
Score = 0
world = pygame.display.set_mode((World_Width, World_Height))
pygame.display.set_caption("Space Shooter")
running = True
Clock = pygame.time.Clock()
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_frect(center = (World_Width / 2, World_Height / 2))
        self.direction = pygame.Vector2()
        self.speed = 300
        self.Can_Shoot = True
        self.last_laser_shot = 0
        self.Laser_Cooldown = 500  
    def laser_Cooldown(self):
        self.Can_Shoot = (pygame.time.get_ticks() - self.last_laser_shot >= self.Laser_Cooldown)
    def update(self, dt):
        Keys = pygame.key.get_pressed()
        self.direction = pygame.Vector2(int(Keys[pygame.K_RIGHT]) - int(Keys[pygame.K_LEFT]) , int(Keys[pygame.K_DOWN]) - int(Keys[pygame.K_UP]))
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt
        Pressed_keys = pygame.key.get_just_pressed()
        if Pressed_keys[pygame.K_SPACE] and self.Can_Shoot:
            Laser((sprites, Laser_spirits), self.rect.midtop)
            self.Can_Shoot = False
            self.last_laser_shot = pygame.time.get_ticks()
        self.laser_Cooldown()
class Star(pygame.sprite.Sprite):
    def __init__(self, groups, Star_surface):
        super().__init__(groups)
        self.image = Star_surface
        self.rect = self.image.get_frect(center = (random.randint(20 , World_Width) , random.randint(20 , World_Height)))

class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, position):
        super().__init__(groups)
        self.image = Laser_surface
        self.rect = self.image.get_frect(midbottom = position)
        self.speed = 1000
        Laser_sound.play()
    
    def update(self, dt):
        self.rect.top -= self.speed * dt
        if self.rect.bottom  < 0:
            self.kill()

class meteor(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = Meteor_surface
        self.rect = self.image.get_frect(center = (random.randint(0, World_Width) , 0))
        self.speed = random.randint(300,  400)
        self.direction = pygame.Vector2(random.uniform(-0.5 , 0.5) , 1)
        self.Life_Time = 7000
        self.Creation_Time = pygame.time.get_ticks()
        self.curr_rotation = 0
        self.rotation_speed = random.randint(40 , 80)
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.Creation_Time > self.Life_Time or self.rect.top > World_Height: 
            self.kill()
        self.curr_rotation += self.rotation_speed * dt
        self.image = pygame.transform.rotate(Meteor_surface , self.curr_rotation)
        self.rect = self.image.get_frect(center = self.rect.center)

class Explosion_Animation(pygame.sprite.Sprite):
    def __init__(self, groups, position):
        super().__init__(groups)
        self.frames = explosion
        self.index = 1
        self.image = self.frames[self.index]
        self.rect = self.image.get_frect(center = position)
        self.timer = pygame.time.get_ticks()
        explosion_sound.play()

    def update(self, dt):
            if self.index > 20:
                self.kill()
                return
            self.image = self.frames[int(self.index)]
            self.index += dt * 20


def Display_Score():
    display = font.render(str(Score), True, (240, 240 , 240))
    display_rect = display.get_frect(topleft = (30 , 30))
    world.blit(display, display_rect)
    pygame.draw.rect(world , 'red' , display_rect.inflate(30 , 20).move(0 , -8) , 5 , 10)
def Collisions():
    global running , Score
    for laser in Laser_spirits:
        if pygame.sprite.spritecollide(laser, meteor_spirits , True, pygame.sprite.collide_mask) :
            Explosion_Animation((sprites), laser.rect.midtop)
            laser.kill()
            Score += 1 
            
    if pygame.sprite.spritecollide(player , meteor_spirits , True, pygame.sprite.collide_mask) :
        player.kill()
        running = False

sprites = pygame.sprite.Group()
meteor_spirits = pygame.sprite.Group()
Laser_spirits = pygame.sprite.Group()

Star_surface = pygame.image.load('images/star.png')
Laser_surface = pygame.image.load('images/laser.png')
Meteor_surface = pygame.image.load('images/meteor.png')
explosion = [pygame.image.load(f'images/explosion/{i}.png') for i in range(21)]
font = pygame.font.Font('images/Oxanium-Bold.ttf', 40)

Laser_sound = pygame.mixer.Sound('audio/Laser.wav')
World_sound = pygame.mixer.Sound('audio/game_music.wav')
explosion_sound = pygame.mixer.Sound('audio/explosion.wav')

World_sound.play(-1)

for i in range(20):
    Star(sprites , Star_surface)
player = Player(sprites)
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)


while running:
    dt = Clock.tick() / 1000
    world.fill('#3a2e3f')
    sprites.update(dt)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == meteor_timer:
            meteor((sprites, meteor_spirits))
    Display_Score()
    Collisions()
    sprites.draw(world)
    pygame.display.update()
pygame.quit()