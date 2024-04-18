from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(3)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        next_position_on_x = self.xcor() + self.x_move
        next_position_on_y = self.ycor() + self.y_move
        self.goto(next_position_on_x, next_position_on_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.setposition(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
