from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.level_text_update()

    def level_text_update(self):
        self.clear()
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_increase(self):
        self.level += 1
        self.level_text_update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!!", align="center", font=FONT)

