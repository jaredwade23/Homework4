from graphics import *

# Create the graphics window
win = GraphWin("Logistic Function", 700, 600)

# Create labels
start_label = Text(Point(100, 40), "Starting Value:")
start_label.draw(win)

k_label = Text(Point(100, 80), "Value of k:")
k_label.draw(win)

# Create entry boxes
start_entry = Entry(Point(200, 40), 10)
start_entry.draw(win)

k_entry = Entry(Point(200, 80), 10)
k_entry.draw(win)

# Create the Graph button
button = Rectangle(Point(300, 25), Point(400, 55))
button.draw(win)

button_text = Text(Point(350, 40), "Graph")
button_text.draw(win)

# Draw the x-axis
x_axis = Line(Point(50, 500), Point(650, 500))
x_axis.draw(win)

# Draw the y-axis
y_axis = Line(Point(50, 120), Point(50, 500))
y_axis.draw(win)

# Wait for the user to click
while True:

    click = win.getMouse()

    # Check if the button was clicked
    if 300 <= click.getX() <= 400 and 25 <= click.getY() <= 55:

        # If the button says Graph
        if button_text.getText() == "Graph":

            # Get the values from the entry boxes
            x = float(start_entry.getText())
            k = float(k_entry.getText())

            # Start with no previous point
            previous_point = None

            # Plot 100 points
            for i in range(100):

                # Calculate the next logistic value
                x = k * x * (1 - x)

                # Convert coordinates to the window
                screen_x = 50 + i * 6
                screen_y = 500 - x * 350

                # Create the current point
                current_point = Point(screen_x, screen_y)

                # Connect to the previous point
                if previous_point != None:
                    line = Line(previous_point, current_point)
                    line.draw(win)

                # Save the current point
                previous_point = current_point

            # Change the button to Exit
            button_text.setText("Exit")

        else:
            # Exit the program
            break

# Close the window
win.close()