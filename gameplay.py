import pygame
import sys
import math

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
clock = pygame.time.Clock()
yellow = (255,246,0)
current_scene = "gameplay"

circles = []  # List to store circles

def create_circle(x, y, radius, color):
    circles.append({"color": color, "center": (x, y), "radius": radius})

def collision(circle1, circle2, circle1rad, circle2rad):
    distance = math.sqrt((circle1[0] - circle2[0]) ** 2 + (circle1[1] - circle2[1])**2)
    if (circle1rad + circle2rad) >= distance:
        return True

def gameplay(player):
    global current_scene, circles
    current_scene = "gameplay"
    screen.fill(yellow)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and clock.tick() >= 15:
        # Create a circle when the spacebar is pressed
        create_circle(player.x + player.valwidth / 2, player.y, 30, (255, 0, 0))
    
    for circle in circles:
        if circle["center"][1] <= -2 * circle["radius"]:
            circles.remove(circle)
        pygame.draw.circle(screen, circle["color"], circle["center"], circle["radius"])
        circle["center"] = (circle["center"][0], circle["center"][1] - player.vel)
           
def get_scene():
    return current_scene
