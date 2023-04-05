import pygame

# Initialize Pygame
pygame.init()

# Set up the window
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ball")

# Set up the ball
ball_radius = 25
ball_color = (255, 0, 0)  # Red
ball_pos = [screen_width // 2, screen_height // 2]  # Start at the center of the screen

# Set up the clock
clock = pygame.time.Clock()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_pos[1] -= 20
            elif event.key == pygame.K_DOWN:
                ball_pos[1] += 20
            elif event.key == pygame.K_LEFT:
                ball_pos[0] -= 20
            elif event.key == pygame.K_RIGHT:
                ball_pos[0] += 20
    
    # Make sure the ball stays on the screen
    ball_pos[0] = max(ball_radius, min(screen_width - ball_radius, ball_pos[0]))
    ball_pos[1] = max(ball_radius, min(screen_height - ball_radius, ball_pos[1]))
    
    # Draw the ball and the background
    screen.fill((255, 255, 255))  # White background
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    
    # Update the screen and wait
    pygame.display.update()
    clock.tick(60)  # Limit to 60 frames per second
