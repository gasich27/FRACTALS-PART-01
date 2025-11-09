import pygame
import random

def run_sierpinski():
    W, H = 900, 800
    POINTS_PER_FRAME = 500
    BG_COLOR = (0, 0, 0)
    FPS = 60

    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("sierpinski triangle")
    clock = pygame.time.Clock()

    vertices = [(0, -1), (-1, 1), (1, 1)]
    x, y = 0.0, 0.0
    zoom = 350
    offset_x, offset_y = W // 2, H // 2
    zoom_speed = 1.1

    dot_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def random_color():
        return (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    def to_screen(px, py):
        return int(px * zoom + offset_x), int(py * zoom + offset_y)

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEWHEEL:
                zoom *= zoom_speed if e.y > 0 else 1 / zoom_speed
                dot_color = random_color()

        for _ in range(POINTS_PER_FRAME):
            vx, vy = random.choice(vertices)
            x = (x + vx) / 2
            y = (y + vy) / 2
            sx, sy = to_screen(x, y)
            if 0 <= sx < W and 0 <= sy < H:
                screen.set_at((sx, sy), dot_color)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


# ничего не запускается при импорте!
if __name__ == "__main__":
    run_sierpinski()
