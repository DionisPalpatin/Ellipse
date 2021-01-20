import pygame as pg
from math import sqrt, ceil

size = 800
rad = 300
y = 0.0
previous_y = int(rad * 0.5)

pg.init()
window = pg.display.set_mode((size, size), pg.SHOWN)
window.fill((255, 255, 255))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.exit()
            exit()

    for x in range(1, rad + 1):
        y = sqrt(rad * rad - (x ** 2)) * 0.5
        y = ceil(y)
        pg.draw.line(window, (0, 0, 0), (size // 2 + x - 1, size // 2 - previous_y), (size // 2 + x, size // 2 - y), 5)
        pg.draw.line(window, (0, 0, 0), (size // 2 + x - 1, size // 2 + previous_y), (size // 2 + x, size // 2 + y), 5)
        pg.draw.line(window, (0, 0, 0), (size // 2 - x + 1, size // 2 - previous_y), (size // 2 - x, size // 2 - y), 5)
        pg.draw.line(window, (0, 0, 0), (size // 2 - x + 1, size // 2 + previous_y), (size // 2 - x, size // 2 + y), 5)
        previous_y = y


    pg.display.update()
    pg.time.delay(10)