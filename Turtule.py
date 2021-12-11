import turtle

tr=turtle.Screen()
tr.bgcolor("blue")
tr.title("Turtule")
pen=turtle.Turtle()
pen.color("White")
pen.fillcolor("green")
side =400
for x in range(8):
  pen.forward(side/4)
  pen.right((side/4)+44)
  pen.back((side / 4) + 44)