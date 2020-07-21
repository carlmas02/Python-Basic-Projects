import turtle
import time
import random


delay = 0.1


#score
score = 0
high_score = 0


#set up the screen

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("grey")
wn.setup(width = 600,height = 600)
wn.tracer(0) #turn off screen updates

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#pen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score = 0 High score = 0" , align="center")


#functions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x =head.xcor()
        head.setx(x+20)



#keyboard binding
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

#main game loop
while True:
    wn.update()

    #check for coliision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor()<-290 or head.ycor() > 290 :
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # hide segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear segments
        segments.clear()

        #reset score
        score = 0
        pen.clear()
        pen.write("Score : {} High score {}".format(score, high_score), align="center")

    #check for collision
    if head.distance(food)<20:
        #move food
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)



        #add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("brown")
        new_segment.penup()
        segments.append(new_segment)

        #inc the score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High score {}".format(score,high_score) ,align= "center" )




    #move end segments
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segments
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()

    # check for head collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear segments list
            segments.clear()

            score = 0
            pen.clear()
            pen.write("Score : {} High score {}".format(score, high_score), align="center")


    time.sleep(delay)


wn.mainloop()
