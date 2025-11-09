import pygame
import math
import random
import imageio.v3 as iio
import numpy as np
import os


def run_pythagoras():
    print("running pythagoras tree...")

    W, H = 1400, 800
    BG = (8, 10, 14)
    L = 150
    D = 13
    BASE_WIDTH = 5
    alpha = 0.5

    COLOR_START = (0, 0, 120)
    COLOR_END = (100, 180, 255)

    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("pythagoras tree")

    branches = []

    def lerp_color(c1, c2, t):
        return (
            int(c1[0] + (c2[0] - c1[0]) * t),
            int(c1[1] + (c2[1] - c1[1]) * t),
            int(c1[2] + (c2[2] - c1[2]) * t)
        )

    def build_tree(x, y, l, angle, depth, level):
        if level == depth:
            return
        x2 = x + math.cos(angle) * l
        y2 = y + math.sin(angle) * l
        branches.append(((x, y), (x2, y2), level))

        l_left = l * math.cos(alpha)
        l_right = l * math.sin(alpha)
        a_left = angle + alpha
        a_right = angle - (math.pi / 2 - alpha)

        build_tree(x2, y2, l_left, a_left, depth, level + 1)
        build_tree(x2, y2, l_right, a_right, depth, level + 1)

    def generate_tree():
        branches.clear()
        build_tree(W // 2, H - 60, L, -math.pi / 2, D, 0)

    def draw_scene():
        screen.fill(BG)
        for (p1, p2, n) in branches:
            t = n / D
            color = lerp_color(COLOR_START, COLOR_END, t)
            width = max(1, int(BASE_WIDTH * (1 - t)))
            pygame.draw.line(screen, color, p1, p2, width)
        pygame.display.flip()

    generate_tree()

    running = True
    clock = pygame.time.Clock()
    frames = []
    record = True

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
                elif e.key == pygame.K_a:
                    alpha -= 0.01
                    generate_tree()
                elif e.key == pygame.K_d:
                    alpha += 0.01
                    generate_tree()

        draw_scene()

        if record:
            frame = pygame.surfarray.array3d(screen).swapaxes(0, 1)
            frames.append(frame.copy())

        clock.tick(30)

    pygame.quit()

    if record and frames:
        os.makedirs("records", exist_ok=True)
        path = os.path.join("records", "pythagoras_tree.mp4")
        print("💾 saving animation...")
        iio.imwrite(path, frames, fps=30, codec="libx264")
        print(f"✅ saved {path}")


if __name__ == "__main__":
    run_pythagoras()
