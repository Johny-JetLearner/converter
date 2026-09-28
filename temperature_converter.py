from tkinter import*
window=Tk()
label=Label(window,text="Celcius->Fahrenheit")
label.place(x=44,y=77)
Leo=Label(window,text="Enter Temperature in Celcius")
Leo.place(x=44,y=100)
entry=Entry(window)
entry.place(x=200,y=100)
def converter():
    entry_get=entry.get()
button=Button(window,text="Convert",command=converter)
button.place(x=120,y=120)
window=mainloop()