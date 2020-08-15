from turtle import *

speed(0)  #speed of turtle we have given 
setup(800,500) #width, height of our screen window

penup()
goto(-400,250)   #we will send our pen to corner and keep down there
pendown()

#now we will draw orangle rectangle

color("orange")
begin_fill()
forward(800) #as our screen width we have taken 800 so we want to fill full our output window
right(90) #turn 90 towards down
forward(167) #we will divide our screen into 3 parts orange, white , green
right(90)
forward(800)
end_fill()
left(90)
forward(167)


#we have our background as white so we dont need to fill that again



#now green
color("green")
begin_fill()
forward(167)
left(90)
forward(800)
left(90)
forward(167)
end_fill()


#now we will make hblue circle in middle of the white frame

penup()
goto(70,0)
pendown()
color("navy")
begin_fill()
circle(70)  #circle of radius 70
end_fill()

#it's not hollow so we will make it hollow by adding the white color  inside blue color
#we fill that circle as a radius of 60

penup()
goto(60,0)  #radius we are taking of 60 so we will choode coordinate accordingly
pendown()
color("white")
begin_fill()
circle(60)
end_fill()


#now we will add small circle on the circumference of the main circle

penup()
goto(-57, -8)
pendown()
color("navy")
for i in range(24):  #there are 24 spokes in the ashok chakraso we will make small bumps by the circle
    begin_fill()
    circle(3)
    end_fill()
    penup()
    forward(15)
    right(15)
    pendown()
    

#now we will make small navy blue circle inside our white circle 
penup()
goto(20,0)
pendown()
begin_fill()
circle(20)
end_fill()



#now adding spokes in our flag
penup()
goto(0,0)
pendown()
pensize(2)
for i in range(24):
    forward(60)
    backward(60)
    left(15)


mainloop()  #to make the turtle window idle.
hideturtle()





