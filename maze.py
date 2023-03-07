from maze_data import *

display.set_caption('Лабіринт')

bg = transform.scale(image.load("background.jpg"), WINDOW_SIZE)

player = Player("hero.png", 5, 325, 325)
enemy = Enemy("cyborg.png", 3, 550, 230)
treasure = GameSprite("treasure.png", 0, 425, 325)

wall_array = [
   Wall((255,255,255), (10,100), 300, 0),
   Wall((255,255,255), (10,100), 200, 100),
   Wall((255,255,255), (100,10), 100, 100),
   Wall((255,255,255), (100,10), 200, 200),
   Wall((255,255,255), (100,10), 300, 200),
   Wall((255,255,255), (10,100), 400, 100),
   Wall((255,255,255), (10,100), 400, 200),
   Wall((255,255,255), (10,100), 400, 300),
   Wall((255,255,255), (10,100), 400, 400),
   Wall((255,255,255), (10,300), 100, 100),
   Wall((255,255,255), (10,100), 300, 300),
   Wall((255,255,255), (10,100), 200, 300),
   Wall((255,255,255), (100,10), 200, 300),
   Wall((255,255,255), (110,10), 200, 400),
   Wall((255,255,255), (10,100), 200, 400),
   Wall((255,255,255), (110,10), 400, 100),
   Wall((255,255,255), (100,10), 600, 100),
   Wall((255,255,255), (100,10), 500, 400),
   Wall((255,255,255), (110,10), 400, 200),
   Wall((255,255,255), (100,10), 500, 320),
   Wall((255,255,255), (10,80), 500, 320),
   Wall((255,255,255), (10,90), 600, 320),
   Wall((255,255,255), (100,10), 600, 200),
]

mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.Font(None, 24)
win = font.render("You won.", True, (0,255,0))
lose = font.render("You lost.", True, (255,0,0))

clock = time.Clock()

game = True
finish = False
while game:
    clock.tick(FPS)
    for e in event.get():
            if e.type == QUIT:
                game = False
    if finish != True:
        window.blit(bg,(0,0))
        player.reset()
        enemy.reset()

        player.move()
        enemy.move()

        player.reset()
        enemy.reset()
        treasure.reset()
        for wall in wall_array:
            wall.reset()
        if sprite.collide_rect(player, treasure):
            finish = True
            window.blit(win, (WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2))
            money.play()
        for wall in wall_array:
            if sprite.collide_rect(player, wall):
                finish = True
                window.blit(lose, (WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2))
                kick.play()
        if sprite.collide_rect(player, enemy):
            finish = True
            window.blit(lose, (WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2))
            kick.play()
        
        display.flip()