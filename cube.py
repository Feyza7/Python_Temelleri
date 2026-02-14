import pygame
import time
import math

# ------------------ Ayarlar ------------------
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("4-7-8 Nefes Egzersizi")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 28)
big_font = pygame.font.SysFont("arial", 42, bold=True)

# Renkler
BG = (15, 18, 25)
CIRCLE = (80, 180, 255)
TEXT = (230, 235, 245)

CENTER = (WIDTH // 2, HEIGHT // 2)
MIN_R = 60
MAX_R = 160

# ------------------ Yardımcı ------------------
def draw(text, sub, radius):
    screen.fill(BG)
    pygame.draw.circle(screen, CIRCLE, CENTER, int(radius), 0)

    t1 = big_font.render(text, True, TEXT)
    t2 = font.render(sub, True, TEXT)

    screen.blit(t1, t1.get_rect(center=(CENTER[0], CENTER[1]-10)))
    screen.blit(t2, t2.get_rect(center=(CENTER[0], CENTER[1]+35)))

    pygame.display.flip()


def animate_phase(seconds, start_r, end_r, title, subtitle):
    start = time.time()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); quit()

        t = time.time() - start
        if t >= seconds:
            break

        # lineer interpolasyon
        ratio = t / seconds
        radius = start_r + (end_r - start_r) * ratio

        draw(title, f"{subtitle} ({int(seconds - t)} sn)", radius)
        clock.tick(60)


# ------------------ Ana Döngü ------------------
running = True
while running:
    # 4 sn nefes al (genişle)
    animate_phase(4, MIN_R, MAX_R, "Nefes Al", "4 saniye")

    # 7 sn tut (sabit)
    animate_phase(7, MAX_R, MAX_R, "Nefesi Tut", "7 saniye")

    # 8 sn nefes ver (daral)
    animate_phase(8, MAX_R, MIN_R, "Nefes Ver", "8 saniye")

    # Kısa ara
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

pygame.quit()