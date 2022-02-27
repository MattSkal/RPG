import pygame
import random

DISTANCE = 20
WIDTH = DISTANCE * 40
HEIGHT = DISTANCE * 30
BACKGROUND = (53, 124, 60)
CHECKERED = (53, 142, 60)
snakeColor = [239, 109, 109]


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game_clock = pygame.time.Clock()
    game_goes_on = True
    snake_head = [random.randrange(DISTANCE * 2, WIDTH - DISTANCE, DISTANCE),
                  random.randrange(DISTANCE * 2, HEIGHT - DISTANCE, DISTANCE)]
    snake = [snake_head, (snake_head[0] + DISTANCE, snake_head[1])]

    dx = random.choice([DISTANCE, 0, -DISTANCE])
    if dx == 0:
        dy = random.choice([DISTANCE, -DISTANCE])
    else:
        dy = 0
    fruit = [random.randrange(DISTANCE, WIDTH, DISTANCE), random.randrange(DISTANCE, HEIGHT, DISTANCE)]
    clockSpeed = 10

    while game_goes_on:
        # process input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_goes_on = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                game_goes_on = False
            if keys[pygame.K_UP] and dy != DISTANCE:
                dx = 0
                dy = -DISTANCE
            if keys[pygame.K_DOWN] and dy != -DISTANCE:
                dx = 0
                dy = DISTANCE
            if keys[pygame.K_LEFT] and dx != DISTANCE:
                dx = -DISTANCE
                dy = 0
            if keys[pygame.K_RIGHT] and dx != -DISTANCE:
                dx = DISTANCE
                dy = 0
            if keys[pygame.K_SPACE]:
                clockSpeed = 20
            else:
                clockSpeed = 10
            if keys[pygame.K_p]:
                clockSpeed = 0

        # update the game state
        snake.insert(0, [snake[0][0] + dx, snake[0][1] + dy])
        snake_head = snake[0]
        if snake_head[0] < 0:
            snake_head[0] = WIDTH - DISTANCE
        if snake_head[0] >= WIDTH:
            snake_head[0] = 0
        if snake_head[1] < 0:
            snake_head[1] = HEIGHT - DISTANCE
        if snake_head[1] >= HEIGHT:
            snake_head[1] = 0

        if fruit == snake[0]:
            for i in range(2):
                snakeColor[i] = random.randint(20, 235)
            fruit = [random.randrange(DISTANCE, WIDTH, DISTANCE), random.randrange(DISTANCE, HEIGHT, DISTANCE)]
            while fruit in snake:
                fruit = [random.randrange(DISTANCE, WIDTH, DISTANCE), random.randrange(DISTANCE, HEIGHT, DISTANCE)]

        else:
            snake.pop()

        if snake[0] in snake[1:]:
            pos = snake.index(snake[0], 1)
            snake = snake[0:pos]

        # render
        screen.fill(BACKGROUND)
        for y in range(0, HEIGHT, DISTANCE*2):
            for x in range(0, WIDTH, DISTANCE*2):
                pygame.draw.rect(screen, CHECKERED, (x, y, DISTANCE, DISTANCE))
        for y in range(DISTANCE, HEIGHT, DISTANCE*2):
            for x in range(DISTANCE, WIDTH, DISTANCE*2):
                pygame.draw.rect(screen, CHECKERED, (x, y, DISTANCE, DISTANCE))

        for part in snake:
            if snake.index(part) % 2 == 0:
                pygame.draw.rect(screen, snakeColor,
                             (part[0], part[1], DISTANCE, DISTANCE))
            else:
                snakeColor[0] -= 20
                pygame.draw.rect(screen, snakeColor,
                                 (part[0], part[1], DISTANCE, DISTANCE))
                snakeColor[0] += 20

        font = pygame.font.Font(None, 74)
        text = font.render(str(len(snake) - 2), 1, 'WHITE')
        screen.blit(text, (WIDTH/2, HEIGHT - DISTANCE * 3))
        pygame.draw.circle(screen, (87, 51, 145), (fruit[0] + DISTANCE // 2, fruit[1] + DISTANCE // 2), DISTANCE // 2)
        pygame.display.update()
        game_clock.tick(clockSpeed)
        print(snakeColor)
    pygame.quit()


if __name__ == '__main__':
    main()
