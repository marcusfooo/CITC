from turtle import *
from random import choice

# Initialise turtles
pen1 = Turtle()
pen1.speed(10) #Set Speed

pen1.color("green") # Set Color
pen1.shape("turtle") # Set Sprite
pen1.penup()
pen1.goto(-200,100) # Goto goal location

pen2 = pen1.clone()
pen2.color("blue")
pen2.penup()
pen2.goto(-200,-100)



# Draw circles
pen1.goto(300,60)
pen1.pendown()
pen1.circle(40)
pen1.penup()
pen1.goto(-200,100)

pen2.goto(300,-140)
pen2.pendown()
pen2.circle(40)
pen2.penup()
pen2.goto(-200,-100)


 
def diceroll():
  die = [1,2,3,4,5,6]
  return choice(die)*20


for i in range(20):
  if pen1.pos() >=(300,100):
    print("Player 1 wins!")
    break
  
  elif pen2.pos() >=(300,-100):
    print("Player 2 wins!")
    break

  else:
    input("Press enter: ")
    pen1.forward(diceroll())
    pen2.forward(diceroll())