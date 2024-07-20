from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.direction = [self.move_up_r, self.move_up_l, self.move_down_l, self.move_down_r]
        self.move_speed = 0.1

    def move_up_r(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def move_up_l(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def move_down_l(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

    def move_down_r(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

    def bounce_on_y(self):
        self.y_move *= -1

    def bounce_on_x(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def reset_position(self):
        self.goto(x= 0, y= 0)
        self.move_speed = 0.1
        self.bounce_on_x()
