import pygame
import sys

# Initialize the pygame library
pygame.init()
# Create the screen
screen = pygame.display.set_mode((640, 480))
# Set the background color
screen.fill((255, 255, 255))
# Create the bricks
bricks = []
for x in range(10):
    for y in range(10):
        brick = pygame.Rect(x * 64, y * 32, 64, 32)
        bricks.append(brick)
# Create the ball
ball = pygame.Rect(320, 240, 16, 16)
# Create the paddle
paddle = pygame.Rect(320, 400, 64, 16)
# Set the ball's speed
ball_x_speed = 10
ball_y_speed = 10
# Set the paddle's speed
paddle_speed = 50  # Increase this value to make the paddle move faster
# Set the game's state
game_state = "playing"
# Create a clock to control the game's speed
clock = pygame.time.Clock()
# Create a font object
font = pygame.font.Font(None, 72)  # Increase this value to make the text bigger
# Start the main loop
while True:
    if game_state == "playing":
        # Check for events
        for event in pygame.event.get():
            # If the user quits the game, exit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If the user presses a key, move the paddle
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle.x -= paddle_speed
                elif event.key == pygame.K_RIGHT:
                    paddle.x += paddle_speed
        # Update the ball's position
        ball.x += ball_x_speed
        ball.y += ball_y_speed
        # Check if the ball hit a brick
        for brick in bricks:
            if ball.colliderect(brick):
                # Remove the brick from the game
                bricks.remove(brick)
                # Change the ball's direction
                ball_x_speed *= -1
                ball_y_speed *= -1
        # Check if the ball hit the paddle
        if ball.colliderect(paddle):
            # Change the ball's direction
            ball_y_speed *= -1
        # Check if the ball hit the left or right edge of the screen
        if ball.x < 0 or ball.x > 640:
            ball_x_speed *= -1
        # Check if the ball hit the top edge of the screen
        if ball.y < 0:
            ball_y_speed *= -1
        # Check if the ball fell off the screen
        if ball.y > 480:
            # Game over
            game_state = "game over"
        # Check if all the bricks are broken
        if not bricks:
            # Game over
            game_state = "game over"
        # Update the screen
        screen.fill((255, 255, 255))
        # Draw the bricks
        for brick in bricks:
            pygame.draw.rect(screen, (0, 0, 0), brick)
        # Draw the ball
        pygame.draw.rect(screen, (255, 0, 0), ball)
        # Draw the paddle
        pygame.draw.rect(screen, (0, 255, 0), paddle)
    elif game_state == "game over":
        # Draw the game over message
        text = font.render("Game Over", True, (255, 165, 0))
        screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    # Update the display
    pygame.display.flip()
    # Slow down the game
    clock.tick(60)
