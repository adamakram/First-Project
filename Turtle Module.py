import turtle

sides = int(input('Please enter the amount of slides'))

length = int(input('Please enter the length you would like to use'))

g= 180*(sides-2)/sides
g=(180-g)

wn = turtle.Screen()


Leonardo = turtle.Turtle()

Raphael = turtle.Turtle()


for i in range(sides):
    Raphael.color('red')
    Raphael.forward(length)
    Raphael.left(g)
    Leonardo.color('blue')
    Leonardo.forward(length)
    Leonardo.left(g)
    Leonardo.color('blue')
    Leonardo.fillcolor('blue')


