import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Car Racing Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clock
clock = pygame.time.Clock()

# Car class
class Car:
    def __init__(self):
        self.image = pygame.Surface((50, 100))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height - 120)
        self.speed = 5

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.speed

    def move_right(self):
        if self.rect.right < width:
            self.rect.x += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

# Obstacle class
class Obstacle:
    def __init__(self):
        self.width = random.randint(40, 80)
        self.height = random.randint(40, 80)
        self.x = random.randint(0, width - self.width)
        self.y = -self.height
        self.color = GREEN
        self.speed = random.randint(3, 7)

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Main function
def game():
    car = Car()
    obstacles = []
    score = 0
    run_game = True

    while run_game:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        # Get keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car.move_left()
        if keys[pygame.K_RIGHT]:
            car.move_right()

        # Create new obstacles
        if random.random() < 0.02:
            obstacles.append(Obstacle())

        # Move and draw obstacles
        for obstacle in obstacles[:]:
            obstacle.move()
            obstacle.draw()
            if obstacle.y > height:
                obstacles.remove(obstacle)
                score += 1

            # Check collision
            if car.rect.colliderect(pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)):
                print(f"Game Over! Final Score: {score}")
                run_game = False

        # Draw the car
        car.draw()

        # Update display
        pygame.display.update()

        # Set frame rate
        clock.tick(60)

# Run the game
game()

# Quit pygame
pygame.quit()
