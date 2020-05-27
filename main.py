import tkinter as tk
from snake import Snake

class Wrapper():
    def __init__(self,x=5,y=10,width=20,height=20):
        root=tk.Tk()
        game_frame=tk.Frame(root)
        Snake(x=x,y=y,width=width,height=height,frame=game_frame)
        root.mainloop()

if __name__=='__main__':
    Wrapper()