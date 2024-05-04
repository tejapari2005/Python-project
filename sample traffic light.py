import pygame
import sys
import math
import time
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the window
WIDTH, HEIGHT = 800, 600

# Define color constraints using a dictionary
COLOR_CONSTRAINTS = {
    "background": (255, 255, 255),    # white
    "road": (0, 0, 0),                # black
    "Line": (255, 255, 255),          # line
    "center_circle": (128, 128, 128), # gray
    "pole": (128, 128, 128),          # gray for poles
    "red": (255, 0, 0),               # red
    "yellow": (255, 255, 0),          # yellow
    "green": (0, 255, 0)              # green
}


# Create a display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TRAFFIC LIGHT STIMULATOR")


# Draw the vertical line at the bottom of the road
def draw_vertical_line_bottom(x, y, width, height, color):
    line_width = 4  # Increase the line width to increase line height
    line_gap = 10    # Adjust the gap between lines as needed
    for i in range(x, x + width, line_gap):  # Loop over the width of the road
        # Start the lines slightly offset from the bottom edge of the road
        for k in range(line_width):
            for j in range(y + height - 950, y + height + 10):  # Start drawing from the bottom edge
                screen.set_at((i + k, j), (255, 255, 255))  # White color













# Function to draw vertical lines in road
def draw_vertical_line_top(x, y, width, height, color):
    # Draw white lines
    line_width = 4  # Increase the line width to increase line height
    line_gap = 10    # Adjust the gap between lines as needed
    for i in range(x, x + width, line_gap):  # Loop over the width of the road
        # Start the lines slightly offset from the top edge of the road
        for k in range(line_width):
            for j in range(y + 5, y + height - 5):
                screen.set_at((i + k, j), (255, 255, 255))  # White color

# Draw the vertical road dividers 
def draw_vertical_road_divider(x, y, width, height, color):
    line_width = 4  # Increase the line width to increase line height
    line_gap = 10  
    for j in range(width, width + height // 2, line_gap):  # Loop over the height of the road
        for i in range(x, x + width):  # Loop over the width of the road
            for k in range(line_width):
                screen.set_at((i + k, j), color)  # Set pixel color
     
 
# Function to draw a road
def draw_road(x, y, width, height, color):
    for i in range(x, x + width):
        for j in range(y, y + height):
            screen.set_at((i, j), color)
            

# Function to draw a circle
def draw_circle(center, radius, color):
    num_points = 20
    points = []
    for i in range(num_points):
        angle = i * (2 * math.pi) / num_points
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        points.append((x, y))
    pygame.draw.polygon(screen, color, points)

# Function to draw poles
def draw_poles(x, y, width, height, color):
    for i in range(x, x + width):
        for j in range(y, y + height):
            screen.set_at((i, j), color)

# Draw the horizontal line at the top of the road
def draw_horizontal_road_divider(x, y, width, height, color):
    line_width = 4  # Increase the line width to increase line height
    line_gap = 10  
    for i in range(width // 2, width, line_gap):  # Loop over the width of the road
        for j in range(y, y + height):  # Loop over the height of the road
            for k in range(line_width):
                screen.set_at((x + i + k, j), color)  # Set pixel color

# Road and center circle Dimensions
road_width = 100
road_height = 2000

# Circle dimensions
circle_radius = 15

# Drawing traffic light poles
pole_width = 10
pole_height = 200
pole_x = WIDTH // 2 - pole_width // 2
pole_y = HEIGHT // 2 - pole_height // 2
            
# Class for Traffic Light
class TrafficLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.colors = [COLOR_CONSTRAINTS["red"], COLOR_CONSTRAINTS["yellow"], COLOR_CONSTRAINTS["green"]]
        self.current_color_index = 0
        self.last_color_change_time = time.time()
        self.time_to_change = random.randint(1, 5)

    def update(self):
        current_time = time.time()
        if current_time - self.last_color_change_time >= self.time_to_change:  # Change color based on individual time
            self.current_color_index = (self.current_color_index + 1) % len(self.colors)
            self.last_color_change_time = current_time
            self.time_to_change = random.randint(1, 5)  # Randomize the next time to change color

    def draw(self):
        # Draw the pole
        draw_poles(self.x, self.y, pole_width, pole_height + 10, COLOR_CONSTRAINTS["pole"])

        # Draw the rectangular box above the pole
        pygame.draw.rect(screen, COLOR_CONSTRAINTS["road"], (self.x - 10, self.y - 50, 30, 100))

        # Draw lights within the rectangle
        light_radius = 10
        light_spacing = 30
        light_y_offset = 20
        for i, _ in enumerate(self.colors):
            light_x = self.x + 5  # Center of the rectangle
            light_y = self.y - 30 + (i * light_spacing)
            if i == self.current_color_index:
                draw_circle((light_x, light_y), light_radius, self.colors[i])
            else:
                draw_circle((light_x, light_y), light_radius, COLOR_CONSTRAINTS["road"])  # Draw black for other colors


# Create traffic lights
traffic_lights = [TrafficLight(pole_x - 120, pole_y - 60), TrafficLight(pole_x + 75, pole_y - 60),
                  TrafficLight(pole_x - 75, pole_y - 160), TrafficLight(pole_x + 120, pole_y - 160)]


# Main Loop
running = True
last_time = time.time()  # Initialize the last time variable outside the loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Setting white screen
    screen.fill(COLOR_CONSTRAINTS["background"])

    # Function calling for drawing road
    draw_road(WIDTH // 2 - road_width // 2, HEIGHT // 2 - road_height // 2, road_width, road_height, COLOR_CONSTRAINTS["road"])  # Horizontal road
    draw_road(WIDTH // 2 - road_height // 2, HEIGHT // 2 - road_width // 2, road_height, road_width, COLOR_CONSTRAINTS["road"])  # Vertical road

    # Function calling for drawing vertical lines
    draw_vertical_line_top(WIDTH - 625 // 2 - road_width + 100 // 2, HEIGHT // 2 - road_height - 90 // 2, road_width - 99, road_height, COLOR_CONSTRAINTS["Line"])  # vertical right
    draw_vertical_line_top(WIDTH - 785 // 2 - road_width + 100 // 2, HEIGHT // 2 - road_height - 90 // 2, road_width - 99, road_height, COLOR_CONSTRAINTS["Line"])  # vertical left
    draw_vertical_line_bottom(WIDTH - 685 // 2 - road_width + 160 // 2, HEIGHT // 2 - road_height // 2, road_width - 99, road_height, COLOR_CONSTRAINTS["Line"])  # vertical right
    draw_vertical_line_bottom(WIDTH - 685 // 2 - road_width - 2 // 2, HEIGHT // 2 - road_height // 2, road_width - 99, road_height, COLOR_CONSTRAINTS["Line"])  # vertical left

    # Function calling for Dividers on road
    draw_horizontal_road_divider(WIDTH // 2 - road_height // 2, HEIGHT // 2 - road_width // 20, road_height, road_width - 99, COLOR_CONSTRAINTS["Line"])  # right road
    draw_horizontal_road_divider(WIDTH // 2 - road_height - 50 // 2, HEIGHT // 2 - road_width // 20, road_height, road_width - 99, COLOR_CONSTRAINTS["Line"])  # left road
    draw_vertical_road_divider(WIDTH - 685 // 2 - road_width + 83 // 2, HEIGHT // 2 - road_height - 90 // 2, road_width - 99, road_height + 10, COLOR_CONSTRAINTS["Line"])  # vertical road

    # Function calling for drawing circle
    draw_circle((WIDTH // 2, HEIGHT // 2), circle_radius, COLOR_CONSTRAINTS["center_circle"])

    # Update and draw traffic lights
    current_time = time.time()
    if current_time - last_time >= 0.1:  # Change color every 0.1 seconds
        for traffic_light in traffic_lights:
            traffic_light.update()
        last_time = current_time

    for traffic_light in traffic_lights:
        traffic_light.draw()

    # Updating display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
