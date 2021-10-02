import turtle
tur = turtle.Turtle()
list= ["yellow","red","blue","green","orange"]
for i in range(200):
  tur.color(list[i%5])
  tur.pensize(i/10+1)
  tur.forward(i)
  tur.left(59)
  
