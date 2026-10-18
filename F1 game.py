import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# 1. Setup the Game Window
WIDTH, HEIGHT = 1000, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spa-Francorchamps (Belgian GP) - Fixed Physics")
clock = pygame.time.Clock()

# Refined Spa-Francorchamps track points
TRACK_POINTS = [
    (530, 680), (250, 680), (170, 630), (220, 570), 
    (380, 560), (460, 510), (490, 450), (530, 410), 
    (650, 310), (860, 120), (910, 130), (920, 170), 
    (880, 230), (790, 280), (740, 340), (630, 370), 
    (510, 410), (440, 460), (430, 510), (480, 550), 
    (560, 550), (640, 510), (720, 520), (800, 570), 
    (840, 650), (780, 700), (650, 700), (610, 660), 
    (570, 700)
]

# 2. Generate the Visual Track
track_img = pygame.Surface((WIDTH, HEIGHT))
track_img.fill((34, 139, 34))  # Green Grass Background

# Generate a standalone Surface strictly for tracking the track mask
mask_surface = pygame.Surface((WIDTH, HEIGHT))
mask_surface.fill((0, 0, 0))  # Black background = Grass

ROAD_WIDTH = 55
# Draw roads on both visual surface and physics surface
pygame.draw.lines(track_img, (50, 50, 50), True, TRACK_POINTS, width=ROAD_WIDTH)
pygame.draw.lines(mask_surface, (255, 255, 255), True, TRACK_POINTS, width=ROAD_WIDTH)

# Fill gaps at the joints
for pt in TRACK_POINTS:
    pygame.draw.circle(track_img, (50, 50, 50), pt, ROAD_WIDTH // 2)
    pygame.draw.circle(mask_surface, (255, 255, 255), pt, ROAD_WIDTH // 2)

# Create a true mathematical pixel mask (White pixels = Valid track)
track_mask = pygame.mask.from_surface(mask_surface)

# Draw Finish Line across the grid straight
pygame.draw.rect(track_img, (255, 255, 255), (450, 652, 6, ROAD_WIDTH))

# Red player car base surface
car_original = pygame.Surface((24, 12), pygame.SRCALPHA)
car_original.fill((255, 0, 0))

# 3. Car Variables
car_x, car_y = 480, 680  # Positioned safely on the grid
car_angle = 180          # Facing left toward La Source
car_speed = 0
max_speed = 6.0
acceleration = 0.05
steering = 4.0

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 4. Input & Driving Mechanics
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        car_speed = min(max_speed, car_speed + acceleration)
    elif keys[pygame.K_DOWN]:
        car_speed = max(-max_speed / 2, car_speed - acceleration)
    else:
        car_speed *= 0.94  # Rolling friction

    # Steer calculation (requires car to be rolling to turn)
    if keys[pygame.K_LEFT] and abs(car_speed) > 0.1:
        car_angle += steering
    if keys[pygame.K_RIGHT] and abs(car_speed) > 0.1:
        car_angle -= steering

    # Map trajectory trigonometry
    radians = math.radians(car_angle)
    car_x += car_speed * math.cos(radians)
    car_y -= car_speed * math.sin(radians) 

    # 5. Robust Mask-Based Collision Check
    # Convert car coordinates to clean integers safely within surface array constraints
    check_x = max(0, min(WIDTH - 1, int(car_x)))
    check_y = max(0, min(HEIGHT - 1, int(car_y)))

    # Checks if the pixel coordinate evaluates to truthy (White track) inside the mask array
    if track_mask.get_at((check_x, check_y)):
        max_speed = 6.0   # Full asphalt race speed
    else:
        max_speed = 1.2   # Instant deep grass sandtrap penalty
        if car_speed > max_speed:
            car_speed *= 0.85 # Immediate braking force on grass

    # 6. Render Current State
    screen.blit(track_img, (0, 0))

    # Compute rotated car transform matrix
    rotated_car = pygame.transform.rotate(car_original, car_angle)
    new_rect = rotated_car.get_rect(center=(car_x, car_y))
    screen.blit(rotated_car, new_rect.topleft)

    pygame.display.flip()
    clock.tick(60) 

pygame.quit()
sys.exit()


