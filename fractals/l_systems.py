import pygame, math, imageio.v3 as iio, os

def generate_lsystem(axiom, rules, iterations):
    res = axiom
    for _ in range(iterations):
        res = "".join(rules.get(ch, ch) for ch in res)
    return res


def run_lsystem(axiom, rules, angle, iterations=7, step=None, name="custom"):
    W, H = 1200, 900
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption(f"l-system: {name}")
    clock = pygame.time.Clock()

    commands = generate_lsystem(axiom, rules, iterations)

    if step is None:
        total_len = len(commands)
        step = max(0.05, min(30000 / total_len, 0.8))

    scale_factor = 1 / 3
    step *= scale_factor

    print(f"[scale] len={len(commands)}, step={step:.4f}")

    x, y = W // 2, int(H * 0.95)
    a = -math.pi / 2
    progress = 0
    growth = max(10, len(commands) // 250)
    frames = []

    bg = (255, 255, 255)
    color = (0, 180, 74)


    def draw_curve(length):
        X, Y, A = x, y, a
        stack = []
        screen.fill(bg)

        for ch in commands[:length]:
            if ch == "F":
                nx = X + math.cos(A) * step
                ny = Y + math.sin(A) * step
                pygame.draw.line(screen, color, (X, Y), (nx, ny), 1)
                X, Y = nx, ny
            elif ch == "+":
                A += math.radians(angle)
            elif ch == "-":
                A -= math.radians(angle)
            elif ch == "[":
                stack.append((X, Y, A))
            elif ch == "]" and stack:
                X, Y, A = stack.pop()

        pygame.display.flip()
        frame = pygame.surfarray.array3d(screen).swapaxes(0, 1)
        frames.append(frame.copy())

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            progress = min(progress + growth, len(commands))
        if keys[pygame.K_s]:
            progress = max(progress - growth, 0)

        draw_curve(progress)
        clock.tick(60)

    pygame.quit()
    os.makedirs("./records", exist_ok=True)
    iio.imwrite(f"./records/{name}.mp4", frames, fps=60, codec="libx264")
    print(f"✅ saved ./records/{name}.mp4")


if __name__ == "__main__":
    rules = {"X": "F[+X]F[-X]+X", "F": "FF"}
    run_lsystem("X", rules, angle=25, iterations=9, name="scaled_tree_small")
