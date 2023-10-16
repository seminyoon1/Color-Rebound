import pygame
import sys
import math

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

pygame.display.set_caption("Color Rebound")

current_scene = "main_menu"

def inCircle(pos1, pos2, radius):
    distance = math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1])**2)
    if radius >= distance:
        return True

def main_menu():
    buttons = [
    {"color": (0, 128, 255), "center": (width*0.7, height*0.6), "radius": 50, "font": 36, "label": "Quit", "action": "button1_action"},
    {"color": (255, 128, 0), "center": (width*0.2, height*0.6), "radius": 50, "font": 36, "label": "Play", "action": "button2_action"},
    ]
    
    screen.fill(white)
    # Button properties
    for button in buttons:
        pygame.draw.circle(screen, button["color"], button["center"], button["radius"])
        font = pygame.font.Font(None, button["font"])
        text = font.render(button["label"], True, (255, 255, 255))
        text_rect = text.get_rect(center=button["center"])
        screen.blit(text, text_rect)

    # Your game logic and drawing code goes here
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for button in buttons:
                    if inCircle(pygame.mouse.get_pos(), button["center"], button["radius"]) == True:
                        # Call the associated action function
                        if button["action"] == "button1_action":
                            button1_action()
                        elif button["action"] == "button2_action":
                            button2_action()

def new_canvas():
    buttons = [
    {"color": (0, 128, 255), "rect": pygame.Rect(350, 250, 100, 50), "font": 36, "label": "Close", "action": "button1_action"},
    ]
    
    screen.fill(white)
    # Button properties
    for button in buttons:
        pygame.draw.rect(screen, button["color"], button["rect"])
        font = pygame.font.Font(None, button["font"])
        text = font.render(button["label"], True, (255, 255, 255))
        text_rect = text.get_rect(center=button["rect"].center)
        screen.blit(text, text_rect)

    # Your game logic and drawing code goes here
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        # Call the associated action function
                        if button["action"] == "button1_action":
                            button1_action()
                        elif button["action"] == "button2_action":
                            button2_action()

# Function for Button 1 action (Quit)
def button1_action():
    pygame.quit()
    sys.exit()

# Function for Button 2 action (Switch to the new canvas)
def button2_action():
    global current_scene
    current_scene = "new_canvas"

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h


white = (255, 255, 255)

running = True
while running:
    if current_scene == "main_menu":
        main_menu()
    elif current_scene == "new_canvas":
        new_canvas()

    pygame.display.flip()