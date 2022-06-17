import turtle


mandala = turtle.Turtle()

# We'll use this to exitonclick().
window = turtle.Screen()

#Project Name.
turtle.title("Petate Mandala Art")

# Set Background.
turtle.bgcolor ("#D291BC") 

# Set the speed
mandala.speed(0)

# Define the number of iterations
n = 39

# The main function
def drawMandala(n):

  for i in range(n):
      mandala.penup()
      mandala.forward(100)
      mandala.left(90)
      mandala.penup()
      mandala.forward (30)
      mandala.left (90)
      mandala.pendown()
      mandala.pencolor ("#3D3635")
      mandala.right (70)
      mandala.forward (70)
      mandala.right (40)
      mandala.forward (50)
      mandala.pencolor ("#3D3635")
      mandala.left (90)
      mandala.pensize(5)
      mandala.forward (100)
      mandala.pencolor ("#3D3635")
      mandala.left(90)
      mandala.forward (100)
      mandala.right (50)
      mandala.forward (70)
      mandala.pensize(10)
      mandala.left (60)
      mandala.pensize(6)
      mandala.forward (65)
      mandala.left (45)
      mandala.forward (120)
      mandala.pencolor ("#3D3635")
      mandala.circle (100)
      mandala.hideturtle() 

def outer():
    out = turtle.Turtle()
    out.pensize(5)
    out.speed(0)
    out.fillcolor('#E6E6FA')
    out.penup()
    out.goto(-120,-360)
    out.begin_fill()
    out.pendown()
    out.circle(355)
    out.end_fill()
    out.hideturtle() 

def inner():
    inn = turtle.Turtle()
    inn.speed(0)
    inn.fillcolor('#D462FF')
    inn.penup()
    inn.goto(-125,-310)
    inn.begin_fill()
    inn.pendown()
    inn.circle(300)
    inn.end_fill()
    inn.hideturtle()

def CircleBorder():
    r = turtle.Turtle()
    r.pensize(3)
    r.speed(0)
    r.hideturtle()
    r.pencolor('#3D3C3A')
    for i in range (91):
        r.penup()
        r.goto(-120, -5)
        r.right(91)
        r.forward(320)
        r.pendown()
        r.circle(27)
        r.hideturtle()


# Perform the main fucntion
outer()
CircleBorder()
inner()
drawMandala(n)



# Exit on user click.
window.exitonclick()
