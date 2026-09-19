from graphics import *
import math

# Get user input
n = int(input("Enter the number of sides: "))
radius = int(input("Enter the radius: "))

# Create graphics window
win = GraphWin("Rotated Polygon", 500, 500)

# Center of the window
center_x = 250
center_y = 250

# Calculate angle between vertices
angle = 360 / n

# Rotate the polygon
rotation = 90

# List to hold vertices
points = []

# Calculate each vertex
for i in range(n):
    theta = math.radians(i * angle + rotation)

    x = center_x + radius * math.cos(theta)
    y = center_y - radius * math.sin(theta)

    points.append(Point(x, y))

# Draw polygon
polygon = Polygon(points)
polygon.draw(win)

# Wait for mouse click
win.getMouse()
win.close()