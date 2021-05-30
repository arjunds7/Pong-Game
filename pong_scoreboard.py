from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        """Create the scoreboard for left and right players"""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Value updation in scoreboard"""
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def r_update_score(self):
        """Update the score in right scoreboard"""
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def l_update_score(self):
        """Update the score in left scoreboard"""
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
