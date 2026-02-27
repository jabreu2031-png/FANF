import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with a color
    window.fill((0, 0, 0))  # Black background

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()