import pygame
import sys


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
        size, pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE, 32)
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
        v = (frames / 16) * 255
        DISPLAYSURF.fill((v, v, v))
        pygame.display.update()
        frames += 1
        CLOCK.tick(60)

if __name__ == '__main__':
    main()
