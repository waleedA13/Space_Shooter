from turtle import Turtle


class Ship(Turtle):
    def __init__(self, position):
        super().__init__()
        self.magazine = []
        self.up()
        self.setheading(90)
        self.setposition(position)
        self.shape("turtle")
        self.color("white")

    def move_left(self):
        self.setx(self.xcor() - 20)

    def move_right(self):
        self.setx(self.xcor() + 20)

    def create_bullet(self):
        bullet = Turtle()
        bullet.up()
        bullet.setheading(90)
        bullet.shape("square")
        bullet.shapesize(.2, .5)
        bullet.color("white")
        bullet.setposition(self.xcor(), self.ycor() + 15)
        self.magazine.append(bullet)
