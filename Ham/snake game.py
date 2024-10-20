from tkinter import*
import random

window=Tk()
window.title("snake Game python")
window.resizable(0,0)


Label(window,text='by harsh',font='arial 20 bold').pack(side=BOTTOM)
score=0
direction='down'
GAME_WIDTH=700
GAME_HEIGHT=500
SPEED=190
SPACE_SIZE=60
BODY_PART=2
SNAKE_COLOR='RED'
FOOD_COLOR='BLUE'
BACKGROUND_COLOR='BLACK'


label=Label(window,text='score:{}'.format(score),font=('consolas',40))
label.pack()

canvas=Canvas(window,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()

class snake:
    def __init__(self) :
        self.body_size=BODY_PART
        self.coordinates=[]
        self.squares=[]

        for i in range(0,BODY_PART):
            self.coordinates.append([0,0])
            for x,y in self.coordinates:
                square=canvas.create_rectangle(x,y,x+SPACE_SIZE,Y+SPACE_SIZE,fill= SNAKE_COLOR,tag='SNAKE')
                self.squares.append(square)


               

window.mainloop()