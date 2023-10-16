import pygame
import sys
import math
import main_menu
import game_selector
import gameplay
from player import Player

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
white = (255, 255, 255)

current_scene = "main_menu"

pygame.display.set_caption("Color Rebound")

def collision(circle1, circle2, circle1rad, circle2rad):
    distance = math.sqrt((circle1[0] - circle2[0]) ** 2 + (circle1[1] - circle2[1])**2)
    if (circle1rad + circle2rad) >= distance:
        return True

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
clock = pygame.time.Clock()
player = Player(screen, width, height)
circles = []

running = True

while running:

    pygame.time.delay(5) 
    keys = pygame.key.get_pressed() 
    
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player.vel
    if keys[pygame.K_RIGHT] and player.x < width - player.valwidth:
        player.x += player.vel
    
    if current_scene == "main_menu":
        main_menu.main_menu()
        current_scene = main_menu.get_scene()
        if keys[pygame.K_SPACE] and clock.tick() >= 15:
            circles.append({"color": (255, 0, 0), "center": ((player.x + player.valwidth/2),player.y), "radius": 30})

        # this is too slow, find a better option using a queue      
        for circle in circles:
            for button in main_menu.buttons:
                if collision(circle["center"], button["center"], circle["radius"], button["radius"]) == True:
                    if button["action"] == "quit":
                        pygame.quit()
                        sys.exit()
                    elif button["action"] == "game_selector":
                        circles = []
                        current_scene = "game_selector"
                        
            if circle["center"][1] <= -2 * circle["radius"]:
                circles.remove(circle)
            pygame.draw.circle(screen, circle["color"], circle["center"], circle["radius"])
            circle["center"] = (circle["center"][0], circle["center"][1] - player.vel)

    elif current_scene == "game_selector":
        game_selector.new_canvas()
        current_scene = game_selector.get_scene()
        if keys[pygame.K_SPACE] and clock.tick() >= 15:
            circles.append({"color": (255, 0, 0), "center": ((player.x + player.valwidth/2),player.y), "radius": 30})
        
         # this is too slow, find a better option using a queue      
        for circle in circles:
            for button in game_selector.buttons:
                if collision(circle["center"], button["center"], circle["radius"], button["radius"]) == True:
                    if button["action"] == "quit":
                        pygame.quit()
                        sys.exit()
                    elif button["action"] == "main_menu":
                        circles = []
                        current_scene = "main_menu"
                    elif button["action"] == "gameplay":
                        circles = []
                        current_scene = "gameplay"
                        
            if circle["center"][1] <= -2 * circle["radius"]:
                circles.remove(circle)
            pygame.draw.circle(screen, circle["color"], circle["center"], circle["radius"])
            circle["center"] = (circle["center"][0], circle["center"][1] - player.vel)

    elif current_scene == "gameplay":
        gameplay.gameplay(player)
        current_scene = gameplay.get_scene()

    player.draw()

    pygame.display.flip()