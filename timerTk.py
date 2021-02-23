import time
from tkinter import *
from tkinter import  messagebox

root = Tk()
root.title('Timer')
root.config(bg='#16a085')
root.geometry('300x300')

#crate the variables
hour = StringVar()
minute = StringVar()
second = StringVar()

#default values
hour.set("00")
minute.set("00")
second.set("00")

#define function
def countdown():
    t =  int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())

    while t > -1:
        mins,secs = divmod(t,60)

        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        time.sleep(1)
        root.update()
        
        if t == 0:
            messagebox.showinfo(message="Timer stop")
        t -= 1

# widgets
timer_label = Label(root,text='Timer',font=('Arial',26,'bold'),bg='#16a085',fg='#34495e').place(x=100,y=30)
hour_entry = Entry(root,textvariable=hour,width=3).place(x=100,y=100)
lbl_1 = Label(root,text=":",font=('Arial',20,'bold'),bg='#16a085',fg='#34495e').place(x=120,y=91)
minute_entry = Entry(root,textvariable=minute,width=3).place(x=140,y=100)
lbl_2 = Label(root,text=":",font=('Arial',20,'bold'),bg='#16a085',fg='#34495e').place(x=160,y=91)
second_entry = Entry(root,textvariable=second,width=3).place(x=180,y=100)
start_button = Button(root,text="Start",font=('Arial'),fg='#16a085',width=10,command=countdown).place(x=100,y=130)


root.mainloop()