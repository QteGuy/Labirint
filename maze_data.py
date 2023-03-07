from pygame import *

SPRITE_SIZE = (65, 65)
WINDOW_SIZE = (700,500)
FPS = 60
LEFT = "LEFT"
RIGHT = "RIGHT"

window = display.set_mode(WINDOW_SIZE)

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, speed, pos_x, pos_y):
        super().__init__()
        self.image = transform.scale(image.load(image_name), SPRITE_SIZE)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    direction = LEFT

    def move(self):
        if self.rect.x <= 410:
            self.direction = RIGHT
        elif self.rect.x >= 540:
            self.direction = LEFT
        
        if self.direction == LEFT:
            self.rect.x -= self.speed
        elif self.direction == RIGHT:
            self.rect.x += self.speed

class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < WINDOW_SIZE[1] - SPRITE_SIZE[1]:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < WINDOW_SIZE[0] - SPRITE_SIZE[0]:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, rgb, size, wall_x, wall_y):
        super().__init__()
        self.rgb = rgb
        self.size = size
        self.image = Surface(self.size)
        self.image.fill(self.rgb)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))