import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")
t.speed(50)

# Draw a circle
t.width(30)
t.penup()
t.goto(0, -300)
t.pendown()
t.circle(300)

# Inside Circle
t.fillcolor("dark blue") 
t.begin_fill() 
t.width(5)
t.penup()
t.goto(0,-200)
t.pendown()
t.circle(200)
t.end_fill()

# Finger
t.pencolor("white")
t.penup()
t.fillcolor("red")
t.begin_fill()
t.goto(-40, -90)
t.pendown()
t.goto(-40, -115)
t.goto(40,-115)
t.goto(40,-70)
t.setpos(0, -85)  
t.setpos(-40, -90)
t.end_fill()
t.begin_fill()
t.setpos(-60, -60)
t.setpos(-109.0,-31.0)
t.setpos(-94.0,-7.0)
t.setpos(-44.0,-22.0)
t.setpos(-44.0,111.0)
t.seth(90)
t.circle(-15, 180)
t.setpos(-12, 0)
t.setpos(-12, 80)
t.seth(90)
t.circle(-11, 180)
t.setpos(10, 0)
t.setpos(10, 80)
t.seth(90)
t.circle(-11, 180)
t.setpos(32, 0)
t.setpos(32, 80)
t.seth(90)
t.circle(-11, 180)
t.setpos(54, 0)
t.setpos(52, -40)
t.setpos(40, -70)
t.end_fill()


# Close the turtle graphics window on click
screen.exitonclick()