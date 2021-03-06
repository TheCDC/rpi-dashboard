import pygame
import sys
import random
import os
# Tell the RPi to use the TFT screen and that it's a touchscreen device
# os.putenv('SDL_VIDEODRIVER', 'fbcon')
# os.putenv('SDL_FBDEV', '/dev/fb1')
# os.putenv('SDL_MOUSEDRV', 'TSLIB')
# os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')


def randcolor():
    return tuple([random.randrange(0, 255) for i in range(3)])


def main():
    pygame.init()
    infoObj = pygame.display.Info()
    WIDTH = int(infoObj.current_w)
    HEIGHT = int(infoObj.current_h)
    # WIDTH = 800
    # HEIGHT = 480
    size = (WIDTH, HEIGHT)
    CLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode(
        size)
    frames = 0
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT or pygame.mouse.get_pressed()[0] == 1:
                # handle a quit with saving
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[pygame.K_q]:
                # handle a quit without saving
                pygame.mixer.quit()
                pygame.quit()
                sys.exit()
        # v = ((frames % 16) / 16) * 255
        if frames % 2 == 0:
            DISPLAYSURF.fill(randcolor())
        pygame.display.update()
        frames += 1
        CLOCK.tick(16)

if __name__ == '__main__':
    main()
