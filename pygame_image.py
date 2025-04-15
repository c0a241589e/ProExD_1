import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png") #練習1
    kk_img = pg.transform.flip(kk_img, True, False) #練習2
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    bg2_img = pg.transform.flip(bg_img, True, False)

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr % 3200
        X = -1
        Y = 0
        screen.blit(bg_img, [-x, 0]) #6
        screen.blit(bg2_img, [-x + 1600, 0]) 
        screen.blit(bg_img, [-x + 3200, 0]) 
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            Y = Y - 1
        if key_lst[pg.K_DOWN]:
            Y = Y + 1
        if key_lst[pg.K_LEFT]:
            X = X - 1
        if key_lst[pg.K_RIGHT]:
            X = X + 2
        kk_rct.move_ip(X, Y)
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200) #5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()