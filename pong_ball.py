from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 16, "normal")


class Ball(Turtle):
    """Create the ball"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.xmove = 10
        self.ymove = 10
        self.ball_pace = 0.1

    def move(self):
        """Move the ball in X and Y directions"""
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounce the ball in Y directions"""
        self.ymove *= -1

    def bounce_x(self):
        """Bounce the ball in X direction"""
        self.xmove *= -1

    def game_over(self):
        """Set the ball to Home position if the game is over"""
        self.setpos(-10, 10)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def reset_position(self):
        """Reset the ball to Home positions"""
        self.setpos(0, 0)
        self.bounce_x()
