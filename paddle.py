from turtle import Turtle, Screen
screen = Screen()
MOVE_DISTANCE = 40
class Paddle(Turtle):

    def __init__(self, position, up_key, down_key):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len= 1, stretch_wid=5)
        self.color("white")
        self.speed("fastest")
        self.goto(position)
        screen.listen()
        screen.onkey(self.move_up, key= up_key)
        screen.onkey(self.move_down, key= down_key)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x= self.xcor() ,y= new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(x= self.xcor() ,y= new_y)
