import tkinter as tk
win = tk.Tk()
y=0

def sayHi():
    global y
    print(y)

win.geometry("200*100")

b = tk.Button(
    win,
    text = 'click here',
    command = sayHi
)
b.pack()

win.mainloop()

