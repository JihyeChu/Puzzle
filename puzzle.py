import pygame
import time

pygame.init()

winSize = [300, 300]
title = 'Puzzle'
done = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
n = 1


#화면 생성
screen = pygame.display.set_mode(winSize)
pygame.display.set_caption(title)

#이벤트 체크 시간
clock = pygame.time.Clock()

#font
font = pygame.font.SysFont("comicsansms", 70)

while not done:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, ',', y)

    screen.fill(WHITE)

    n = 1
    for y in range(0, 3):
        for x in range(0, 3):
            #rect(screen, 색, 칸(x, y, 칸 가로,세로), 선굵기)
            pygame.draw.rect(screen, BLACK, [x*100, y*100, 100, 100], 1)
            if n == 9:
                continue
            text = font.render(str(n), True, (255, 165, 0))
            n += 1
            screen.blit(text, (x*100, y*100))

    
    pygame.display.flip()

#화면 닫기
pygame.quit()

