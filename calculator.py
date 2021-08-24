from tkinter import *
def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value=eval(screen.get())

            except Exception as e:
                print(e)
                scvalue.set("Error")
                screen.update()
           
             
               
        scvalue.set(value)
        screen.update()    

    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("500x900")
root.title("calculator by pranjul")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar = scvalue, bg = "orange", font = "lucida 40 bold")
screen.pack(fill = X, ipadx = 8, padx = 10, pady = 10)

f = Frame(root, bg = "yellow")
b = Button(f, text = "9", bg = "blue", padx = 20, pady = 20, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
b = Button(f, text = "8", bg = "blue", padx = 20, pady = 20, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
b = Button(f, text = "7", bg = "blue", padx = 20, pady = 20, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
b = Button(f, text = "=", bg = "blue", padx = 20, pady = 20, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
f.pack()

f = Frame(root, bg = "yellow")
b = Button(f, text = "6", bg = "blue", padx = 20, pady = 20, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
b = Button(f, text = "5", bg = "blue", padx = 20, pady = 20, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
b = Button(f, text = "4", bg = "blue", padx = 20, pady = 20, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
b = Button(f, text = "*", bg = "blue", padx = 20, pady = 20, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
f.pack()


f = Frame(root, bg = "yellow")
b = Button(f, text = "3", bg = "blue", padx = 20, pady = 20, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
b = Button(f, text = "2", bg = "blue", padx = 20, pady = 20, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
b = Button(f, text = "1", bg = "blue", padx = 20, pady = 20, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
b = Button(f, text = "/", bg = "blue", padx = 20, pady = 20, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
f.pack()

f = Frame(root, bg = "yellow")
b = Button(f, text = "0", bg = "blue", padx = 20, pady = 20, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
b = Button(f, text = "+", bg = "blue", padx = 20, pady = 20, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
b = Button(f, text = "-", bg = "blue", padx = 20, pady = 20, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
b = Button(f, text = "c", bg = "blue", padx = 20, pady = 20, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
f.pack()
b = Button(f, text = ".", bg = "blue", padx = 20, pady = 12, font = "lucida 30 bold")
b.pack(side = LEFT, padx = 20, pady = 20)
b.bind("<Button>", click)
f.pack()

 







root.mainloop()
