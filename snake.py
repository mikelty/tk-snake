from random import choice

class Snake():
    def __init__(self,x=5,y=10,dx=1,dy=0,tail_x=10,width=20,height=20,frame=None):
        """
        :param x: x coordinate of the head of snake
        :param y: y coordinate of the head of snake
        :param width: width of world
        :param height: height of world
        :param frame: frame of world (tkinter)
        """
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.length=abs(x-tail_x)
        self.width=width
        self.height=height
        self.frame=frame
        self.body=[(self.x+i,self.y) for i in range(self.length)]
        self.body_set=set(self.body)
        self.lost=False
        self.won=False
        self.length=3

    def move(self):
        """
        moves the snake one block, eat food if exists on that block
        :return: None
        """
        if self.valid_move():


    def spawn_food(self):
        empty_spaces = [r * self.width + c for r in range(self.height) for c in range(self.width) \
                        if not self.state[r][c]]
        food=choice(empty_spaces)
        self.state[food//self.width][food%self.width]=True
