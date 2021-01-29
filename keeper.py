from tkinter import*
from random import randint

score=0
r=25
game_flag=True
speed=randint(2,7)
v=7

def motion():
    global ball, score, game_flag,speed,v
    if game_flag:    
        x1,y1,x2,y2=c.coords(ball)    
        if y2<550:
            c.move(ball,0,speed)
        else:
            if c.coords(paddle)[0]<x2<c.coords(paddle)[2]:
                score+=1
                c.itemconfig(score_text,text='Счёт: {}'.format(score))
                x=randint(10,270)
                c.delete(ball)
                ball=c.create_oval(x,5,x+r,30,fil='#9966cc',outline='#f5f5dc')
                speed=randint(2,7)
                v+=1
            else:
                game_flag=False
                c.create_text(130,260,text='Игра Окончена',fil='#f5f5dc',font=('Arial',25,'bold'))
    a.after(20,motion)

def left(event):
    if c.coords(paddle)[0]>0:
        c.move(paddle,-v,0)

def right(event):
    if c.coords(paddle)[2]<300:
        c.move(paddle,v,0)

a=Tk()
a.title('Вратарь')
a.iconbitmap('images/icon.ico')
a.geometry('300x600+500+30')
a.resizable(width=False,height=False)

c=Canvas(a,width=300,height=600,bg='#98777b')
c.pack()
c.create_rectangle(0,550,300,600,fil='#f5f5dc',outline='#f5f5dc')

x=randint(10,270)
ball=c.create_oval(x,5,x+r,30,fil='#9966cc',outline='#f5f5dc')
paddle=c.create_rectangle(120,550,180,570,fil='#9dff00',outline='white')

score_text=c.create_text(240,580,text='Счёт: {}'.format(score),fil='blueviolet',font=('Arial',14,'bold'))

a.bind('<Left>',left)
a.bind('<Right>',right)

motion()
a.mainloop()
