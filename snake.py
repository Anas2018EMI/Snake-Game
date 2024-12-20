from turtle import Turtle

MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
STARTING_POSITIONS=[(0,0), (0,-20),(0,-40)]

class Snake:
    def __init__(self):
        self.block_num=3
        self.blocks=[]
        self.build_snake_item()
        self.head= self.blocks[0]
    
    def build_snake_item(self):
        for block_pos in STARTING_POSITIONS:
            self.add_block(block_pos)     
        
    def add_block(self, block_pos):
        snake_block=Turtle(shape="square")
        snake_block.color("white")
        snake_block.penup()
        snake_block.setpos(block_pos)
        self.blocks+=[snake_block]

    def reset(self):
        self.blocks.clear()
        self.build_snake_item()
        self.head= self.blocks[0]

    
    def extend(self):
        self.add_block(self.blocks[-1].position())
        
    def move(self):
        
        for block_num in range(len(self.blocks)-1, 0, -1 ):
            xcor=self.blocks[block_num-1].xcor()
            ycor=self.blocks[block_num-1].ycor()
            self.blocks[block_num].setpos(xcor, ycor)
        
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    
