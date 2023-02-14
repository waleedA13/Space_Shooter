from turtle import Screen
from time import sleep
from ship import Ship

screen = Screen()
screen.setup(600, 600, 0, 0)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

player = Ship((0, -250))
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "d")
screen.onkey(player.create_bullet, "space")


game_on = True
while game_on:
    screen.update()
    sleep(.1)
    for shot in player.magazine:
        shot.forward(10)


screen.exitonclick()


