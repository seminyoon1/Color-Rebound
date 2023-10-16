import pygame
import sys
import math

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
yellow = (255,246,0)

current_scene = "main_menu"

buttons = [
    {"color": (0, 128, 255), "center": (width*0.7, height*0.6), "radius": 50, "font": 36, "label": "Quit", "action": "quit"},
    {"color": (255, 128, 0), "center": (width*0.2, height*0.6), "radius": 50, "font": 36, "label": "Play", "action": "game_selector"},
    ]

def mouseCircle(pos1, pos2, radius):
    distance = math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1])**2)
    if radius >= distance:
        return True

def main_menu():
    global current_scene
    current_scene = "main_menu"
    screen.fill(yellow)
    # Button properties
    for button in buttons:
        pygame.draw.circle(screen, button["color"], button["center"], button["radius"])
        font = pygame.font.Font(None, button["font"])
        text = font.render(button["label"], True, (255, 255, 255))
        text_rect = text.get_rect(center=button["center"])
        screen.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for button in buttons:
                    if mouseCircle(pygame.mouse.get_pos(), button["center"], button["radius"]) == True:
                        # Call the associated action function
                        if button["action"] == "quit":
                            pygame.quit()
                            sys.exit()
                        elif button["action"] == "game_selector":
                            current_scene = "game_selector"

def get_scene():
    return current_scene
