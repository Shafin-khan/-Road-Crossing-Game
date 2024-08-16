from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

        self.shape("turtle")

        self.fillcolor('black')


        self.go_to_start()
        self.left(90)
        self.showturtle()


    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_it_finishline(self):
        if self.ycor()>FINISH_LINE_Y:
            return  True




