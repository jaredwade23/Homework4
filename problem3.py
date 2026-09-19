from graphics import *

# Get values from user
x = float(input("Enter the starting x value: "))
k = float(input("Enter the value of k: "))

# Create window
win = GraphWin("Logistic Function", 700, 500)

# Draw x-axis
x_axis = Line(Point(50, 450), Point(650, 450))
x_axis.draw(win)

# Draw y-axis
y_axis = Line(Point(50, 50), Point(50, 450))
y_axis.draw(win)

# Plot 100 points
for i in range(100):

    # Calculate next logistic value
    x = k * x * (1 - x)

    # Convert values to screen coordinates
    screen_x = 50 + i * 6
    screen_y = 450 - x * 400

    point = Point(screen_x, screen_y)
    point.draw(win)

# Wait for mouse click
win.getMouse()
win.close()