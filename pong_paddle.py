from turtle import Turtle

PADDLE_HEIGHT = 1
PADDLE_WIDTH = 5


class Paddle(Turtle):

    def __init__(self, position):
        """Create the paddle"""
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.color("white")
        self.setpos(position)
        self.shapesize(stretch_len=PADDLE_HEIGHT, stretch_wid=PADDLE_WIDTH)

    def paddle_go_up(self):
        """Paddle movement in UP direction"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddle_go_down(self):
        """Paddle movement in DOWN direction"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
