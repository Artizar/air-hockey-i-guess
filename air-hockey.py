import turtle
screen= turtle.Screen()
screen.setup(height=600,width=800)
screen.bgcolor("lightblue")
screen.tracer(0)

#line1.shapesize(50,2)
#line1.color("white")
#line1.penup()
#line1.goto(1,0)

goal1= turtle.Turtle()
goal1.shape("square")
goal1.shapesize(50,1)
goal1.color("black")
goal1.speed(0)
goal1.penup()
goal1.goto(400,0)

goal2= turtle.Turtle()
goal2.shape("square")
goal2.shapesize(50,1)
goal2.color("black")
goal2.speed(0)
goal2.penup()
goal2.goto(-400,0)

player1= 0
player2= 0

score= turtle.Turtle()
score.color('green')
score.speed(0)
score.penup()
score.goto(0,250)
score.write("player1:"+ str(player1)+"       player2:"+ str(player2),align ="center",font =("arial",20,"bold"))
score.hideturtle()




pad1= turtle.Turtle()
pad1.shape("square")
pad1.shapesize(5,1)
pad1.color("white")
pad1.speed(0)
pad1.penup()
pad1.goto(390,0)

pad2= turtle.Turtle()
pad2.shape("square")
pad2.shapesize(5,1)
pad2.color("white")
pad2.speed(0)
pad2.penup()
pad2.goto(-390,0)

baller= turtle.Turtle()
baller.shape("circle")
baller.shapesize(1,1)
baller.color('red')
baller.speed(0)
baller.penup()
baller.goto(0,0)
ballerx =0.5
ballery =0.5
def up1():
    Y1=pad1.ycor()
    Y1+=50
    if Y1>250:
        Y1-=50
    pad1.sety(Y1)
def down1():
    Y2=pad1.ycor()
    Y2-=50
    if Y2<-250:
        Y2+=50
    pad1.sety(Y2)
def up2():
    Y1=pad2.ycor()
    Y1+=50
    if Y1>250:
        Y1-=50
    pad2.sety(Y1)
def down2():
    Y2=pad2.ycor()
    Y2-=50
    if Y2<-250:
        Y2+=50
    pad2.sety(Y2)
screen.listen()
screen.onkeypress(up1,"Up")
screen.onkeypress(down1,"Down")
screen.onkeypress(up2,"w")
screen.onkeypress(down2,"s")
while True:
    baller.setx(baller.xcor()+ballerx)
    if baller.xcor()>390:
        score.clear()
        player1 += 1
        score.write("player1:" + str(player1) + "       player2:" + str(player2), align="center",font=("arial", 20, "bold"))
        ballerx = ballerx * -1


    if baller.xcor()<-390:
        score.clear()
        player2 += 1
        score.write("player1:" + str(player1) + "       player2:" + str(player2), align="center",font=("arial", 20, "bold"))
        ballerx = ballerx * -1

    baller.sety(baller.ycor()+ballery)
    if baller.ycor()>290:
        ballery= ballery*-1
    if baller.ycor()<-290:
        ballery= ballery*-1

    if baller.xcor() > 370  and baller.ycor() < pad1.ycor() + 50 and baller.ycor() > pad1.ycor() - 50:
        baller.setx(baller.xcor()+ ballerx)
        ballerx = ballerx*-1

    if baller.xcor() <-370 and baller.ycor() > pad2.ycor() -50 and baller.ycor() < pad2.ycor() + 50:
        baller.setx(baller.xcor() + ballerx)
        ballerx= ballerx*-1

    baller.setx(baller.xcor()+ ballerx)




    screen.update()