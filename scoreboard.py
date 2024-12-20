from re import S
from turtle import Turtle

ALIGNEMENT='center'
FONT=('Courier', 18, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0

        with open('data.txt') as file:
            self.high_score= int(file.read())

        self.color("white")
        self.penup()
        self.setpos(0, 270)
        self.hideturtle()
        self.display_scoreboard()

    def display_scoreboard(self):
        self.clear()
        self.write( f"Score: {self.score} High score: {self.high_score}", False, ALIGNEMENT, FONT)
  
    def refresh_score(self):
        self.score += 1
        self.display_scoreboard()
       
    def reset(self):
        if self.score > self.high_score:
            self.high_score= self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.score))
        
        # self.score=0
        self.display_scoreboard()

    def game_over(self):
        self.setpos(0, 0)
        self.write( f"GAME OVER", False, ALIGNEMENT, FONT)

