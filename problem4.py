from graphics import *

# Get values from the user
x = float(input("Enter the starting value: "))
k = float(input("Enter the value of k: "))

# Create the graphics window
win = GraphWin("Logistic Function", 700, 500)

# Draw the x-axis
x_axis = Line(Point(50, 450), Point(650, 450))
x_axis.draw(win)

# Draw the y-axis
y_axis = Line(Point(50, 50), Point(50, 450))
y_axis.draw(win)

# Start with no previous point
previous_point = None

# Plot 100 points
for i in range(100):

    # Calculate the next logistic value
    x = k * x * (1 - x)

    # Convert the coordinates to the graphics window
    screen_x = 50 + i * 6
    screen_y = 450 - x * 400

    # Create the current point
    current_point = Point(screen_x, screen_y)

    # Connect the current point to the previous point
    if previous_point != None:
        line = Line(previous_point, current_point)
        line.draw(win)

    # Save the current point
    previous_point = current_point

# Wait for a mouse click
win.getMouse()

# Close the window
win.close()