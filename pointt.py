import turtle


class Score(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color('green')
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.score1 = 0
        self.score2 = 0
def upDate(self):
    self.clear()
    self.write('Player1:'+str(self.score1) + ' = Player2:' + str(self.score2),align='center',font = ('Arial',24,'normal'))
def changeScore1(self):
    self.score1 += 1
    self.upDate()
def changeScore2(self):
    self.score2 += 1
    self.upDate()
    if self.xcor() > 350:
        score.changeScore1()
        self.dx *= -1
    if self.xcor() < -350:
        score.changeScore2()
        self.dx *= -1

    if __name__=='__main__':
        screen = turtle.Screen()
        screen.setup(800,600)
        screen.title('Ping Pong')
        screen.tracer(0)
    player1 = Player(-350,0,'red')
    player2 = Player(350,0,'blue')
    ball = Ball(0,0,'yellow')
    score = Score()
    turtle.listen()
    turtle.onkey(player1.moveUp,'w')
    turtle.onkey(player1.moveDown,'s')
    turtle.onkey(player2.moveUp,'Up')
    turtle.onkey(player2.moveDown,'Down')
    while True:
        time.sleep(1/math.pow(10,20))
        screen.update()
        ball.move()
        if score.score2 == 100:
            print('Player2 Win')
            break
        if score.score1 == 100:
            print('Player2 Win')
            break
