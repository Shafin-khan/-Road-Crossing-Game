# Road-Crossing Game
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)


my_turtle = Player()
mycar = CarManager()
scoreboard = Scoreboard()

screen.tracer(0)
# ToDo 1: Making a turtle (done)

# ToDo 2: Move Forward the turtle  (done)

# ToDo 3:Randomly generating car along the y-axis  (done)

# ToDo 4: Moving the car from left to right   (done)

# ToDo 5: Moving back the turtle to its original position
      # increase  the level
      # increase the caar spead

# ToDo 6:detect collides between car and turtle
        #Game is over
        #Stop everything

screen.listen()
screen.onkey(my_turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()

    mycar.car_producer()
    mycar.move_car()

    for car in mycar.all_cars:
        if car.distance(my_turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if my_turtle.is_it_finishline():
        my_turtle.go_to_start()
        mycar.level_up()
        scoreboard.increase_level()
screen.exitonclick()
