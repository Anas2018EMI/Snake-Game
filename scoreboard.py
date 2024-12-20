from turtle import Turtle

ALIGNEMENT='center'
FONT=('Courier', 18, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.setpos(0, 270)
        self.hideturtle()
        self.write( f"Score: {self.score}", False, ALIGNEMENT, FONT)

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.write( f"Score: {self.score}", False, ALIGNEMENT, FONT)
    
    def game_over(self):
        self.setpos(0, 0)
        self.write( f"GAME OVER", False, ALIGNEMENT, FONT)

