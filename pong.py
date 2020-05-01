import turtle


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# poäng
score_a = 0
score_b = 0



# paddel a
paddel_a = turtle.Turtle()
paddel_a.speed(0)
paddel_a.shape("square")
paddel_a.color("white")
paddel_a.shapesize(stretch_wid=5,stretch_len=1)
paddel_a.penup()
paddel_a.goto(-350, 0)



# paddel b
paddel_b = turtle.Turtle()
paddel_b.speed(0)
paddel_b.shape("square")
paddel_b.color("white")
paddel_b.shapesize(stretch_wid=5,stretch_len=1)
paddel_b.penup()
paddel_b.goto(350, 0)



# bollen
boll = turtle.Turtle()
boll.speed(0)
boll.shape("square")
boll.color("white")
boll.penup()
boll.goto(0,0)
boll.dx = 0.1
boll.dy = 0.1


# penna 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Spelare A: 0  Spelare B: 0", align="center", font=("Courier", 24, "normal"))



# upp och ned funktioner
def paddel_a_up():
    y = paddel_a.ycor()
    y += 20
    paddel_a.sety(y)

def paddel_a_down():
    y = paddel_a.ycor()
    y -= 20
    paddel_a.sety(y)

def paddel_b_up():
    y = paddel_b.ycor()
    y += 20
    paddel_b.sety(y)

def paddel_b_down():
    y = paddel_b.ycor()
    y -= 20
    paddel_b.sety(y)


# tangetbord 
wn.listen()
wn.onkeypress(paddel_a_up, "w")
wn.onkeypress(paddel_a_down, "s")
wn.onkeypress(paddel_b_up, "o")
wn.onkeypress(paddel_b_down, "l")





while True:
    wn.update()


    # rörelse på bollen
    boll.setx(boll.xcor() + boll.dx)
    boll.sety(boll.ycor() + boll.dy)

    # när bollen träffar kanten
    if boll.ycor() > 290:
        boll.sety(290)
        boll.dy *= -1

    if boll.ycor() < -290:
        boll.sety(-290)
        boll.dy *= -1

    if boll.xcor() > 390:
        boll.goto(0, 0)
        boll.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Spelare A: {}  Spelare B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if boll.xcor() < -390:
        boll.goto(0, 0)
        boll.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Spelare A: {}  Spelare B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # paddel och boll
    if boll.xcor() < -340 and boll.ycor() < paddel_a.ycor() + 50 and boll.ycor() > paddel_a.ycor() - 50:
       boll.dx *= -1 
    
    if boll.xcor() > 340 and boll.ycor() < paddel_b.ycor() + 50 and boll.ycor() > paddel_b.ycor() - 50:
        boll.dx *= -1