#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Tiffany Schmok
#Date
#12/19/19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game


#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl 


#create turtle
drawer = trtl.Turtle()

#turtle details
pen_size = 1
drawer.shape("arrow")
drawer.shapesize(1)
drawer.pensize(pen_size)


#movement functions

#make turtle go up
def Up():
    drawer.setheading(90)
    drawer.forward(10)

#make turtle go down
def Down():
    drawer.setheading(270)
    drawer.forward(10)

#make turtle go left
def Left():
    drawer.setheading(180)
    drawer.forward(10)

#make turtle go right   
def Right():
    drawer.setheading(0)
    drawer.forward(10)

#make turtle clear drawings
def Clear():
    drawer.clear()


#Change size functions

#make pen size bigger
def Click_O():
    global pen_size
    pen_size += 1
    drawer.pensize(pen_size)

#make pen size smaller
def Click_p():
    global pen_size
    pen_size -= 1
    drawer.pensize(pen_size)

#Pen up or down functions
def Click_u():
   # drawer.up()

#this part is me trying to figure out how to 
#do the isdown thing, but I don't know how to word it :)
    if drawer.isdown() is True:
        drawer.up()
    elif drawer.isdown()is False:
        drawer.down()

#pen down
#def Click_d():
    #drawer.down()

#color/drawing functions

#change pencolor to red
def Color_red():
    drawer.pencolor("red")

#change pencolor to green
def Color_green():
    drawer.pencolor("green")

#change pencolor to blue
def Color_blue():
    drawer.pencolor("blue")

#change pencolor to violet
def Color_violet():
    drawer.pencolor("violet")

#create screen
wn = trtl.Screen()

#bind to keypresses
wn.onkeypress(Up, "Up")
wn.onkeypress(Down, "Down")
wn.onkeypress(Left, "Left")
wn.onkeypress(Right, "Right")
wn.onkeypress(Clear, "space")
wn.onkeypress(Click_O, "o")
wn.onkeypress(Click_p, "p")
wn.onkeypress(Click_u, "u")
wn.onkeypress(Color_red, "r")
wn.onkeypress(Color_green, "g")
wn.onkeypress(Color_blue, "b")
wn.onkeypress(Color_violet, "v")
#wn.onkeypress(Click_d, "d")

#listen
wn.listen()

#mainloop
wn.mainloop()