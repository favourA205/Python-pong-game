

import turtle
wn = turtle.Screen()
wn.title("pong by flame favor")
wn.setup(width=900,height=600)
wn.bgcolor("green")
wn.tracer(0)
# score
score_a = 0
score_b = 0

# bat a
bat_a = turtle.Turtle()
bat_a.speed(10)
bat_a.shape("square")
bat_a.shapesize(stretch_len=1,stretch_wid=5)
bat_a.color("white")
bat_a.up()
bat_a.goto(-400,0)


# bat b
bat_b = turtle.Turtle()
bat_a.speed(10)
bat_b.shape("square")
bat_b.shapesize(stretch_len=1,stretch_wid=5)
bat_b.color("white")
bat_b.up()
bat_b.goto(400,0)


# ball
ball = turtle.Turtle()
bat_a.speed(10)
ball.shape("circle")
ball.color("yellow")
ball.up()
ball.goto(0,0)
ball.dx = 0.8
ball.dy = 0.8

#pen
pen = turtle.Turtle()
pen.speed()
pen.color("white")
pen.penup()
pen.goto(0 , 260)
pen.write(" Player A: 0  Player B: 0 ", align= "center", font= ("courier", 24 ,"normal"))
pen.hideturtle()

# movement of bats
def bat_a_up():
    y = bat_a.ycor()
    y = y + 50
    bat_a.sety(y)
def bat_a_down():
    y = bat_a.ycor()
    y = y - 50
    bat_a.sety(y)
def bat_b_up():
    y = bat_b.ycor()
    y = y + 50
    bat_b.sety(y)
def bat_b_down():
    y = bat_b.ycor()
    y = y - 50
    bat_b.sety(y)
# keyboard binding
wn.listen()
wn.onkeypress(bat_a_up,"f")
wn.onkeypress(bat_a_down,"j")
wn.onkeypress(bat_b_up,"Up")
wn.onkeypress(bat_b_down,"Down")




# main game loop
while True:
    wn.update()
# movement of ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

# border checking
    if ball.ycor() > 300:
        ball.sety(300)
        ball.dy *=-1
    if ball.ycor() < -300:
        ball.sety(-300)
        ball.dy *=-1
    if ball.xcor() > 450:
        ball.goto(0,0)
        ball.dx *=-1
        score_a += 1
        pen.clear()
        pen.write(" Player A: {}  Player B: {}". format(score_a,score_b), align="center", font=("courier", 24, "normal"))
    if ball.xcor() < -450:
        ball.goto(0,0)
        ball.dx *=-1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))


# ball and bat collisions
    if ball.xcor()>380 and (ball.xcor()<390) and (ball.ycor()<(bat_b.ycor() + 40)) and (ball.ycor()>(bat_b.ycor() - 60)):
        ball.setx(380)
        ball.dx *= -1
    if ball.xcor()<-380 and (ball.xcor()<-390) and (ball.ycor()<(bat_a.ycor() + 40)) and (ball.ycor()>(bat_a.ycor() - 60)):
        ball.setx(-380)
        ball.dx *= -1



































































