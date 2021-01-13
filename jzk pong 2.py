
import turtle
# screen
wn = turtle.Screen()
wn.bgcolor("green")
# wn.speed()
wn.setup(width =900,height=600)
wn.tracer(0)


# bat_a
bat_a = turtle.Turtle()
bat_a.speed()
bat_a.shape("square")
bat_a.color("white")
bat_a.shapesize(stretch_len=1,stretch_wid=5)
bat_a.penup()
bat_a.goto(-400,0)


# bat_b
bat_b = turtle.Turtle()
bat_b.speed()
bat_b.shape("square")
bat_b.color("white")
bat_b.shapesize(stretch_len=1,stretch_wid=5)
bat_b.penup()
bat_b.goto(400,0)


# ball

ball = turtle.Turtle()
ball.speed(-0)
ball.shape("circle")
ball.color("orange")
ball.shapesize(stretch_len=1,stretch_wid=1)
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1

# score
score_a = 0
score_b = 0

# pen
pen = turtle.Turtle()
pen.speed()
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center",font=("courier",24,"normal"))
pen.hideturtle()


# movement of bats
def bat_a_up():
    y = bat_a.ycor()
    y = y + 40
    bat_a.sety(y)
def bat_a_down():
    y = bat_a.ycor()
    y = y -40
    bat_a.sety(y)
def bat_b_up():
    y = bat_b.ycor()
    y = y + 40
    bat_b.sety(y)
def bat_b_down():
    y = bat_b.ycor()
    y = y - 30
    bat_b.sety(y)


# keyboard binding

wn.listen()
wn.onkeypress(bat_a_up,"j")
wn.onkeypress(bat_a_down,"f")
wn.onkeypress(bat_b_up,"Up")
wn.onkeypress(bat_b_down,"Down")

# ball movement


# main game loop
while True:
    wn.update()

# ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# border checking
    if ball.ycor() > 300:
        ball.sety(300)
        ball.dy *= -1
    if ball.ycor() < -300:
        ball.sety(-300)
        ball.dy *= -1
    if ball.xcor() > 450:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("courier", 24, "normal"))


    if ball.xcor() < -450:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

# ball and bat collision
    if ball.xcor()> 390 and (ball.xcor() < 400) and (ball.ycor()<bat_b.ycor() +40)  and (ball.ycor()>bat_b.ycor() - 40):
        ball.setx(390)
        ball.dx *= -1
    if ball.xcor()< -390 and (ball.xcor() > -400) and (ball.ycor()<bat_a.ycor() +40)  and (ball.ycor()>bat_a.ycor() - 40):
        ball.setx(-390)
        ball.dx *= -1



   #     'period':period_names,
    #    'short_descriptions':short_descriptions,
    #    'temperatures': temperatures,
   # })
#print(weather_stuff)

#weather_stuff.to_csv('weather.csv')

















