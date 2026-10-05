from tkinter import*
window=Tk()
label=Label(window,text="Enter the weight in Kg")
label.place(x=44,y=77)
Leonardo=Label(window,text="Gram    Pounds    Ounce")
Leonardo.place(x=44,y=140)
entry=Entry(window)
entry.place(x=53,y=100)
def converter():
    entry_get=entry.get()
button=Button(window,text="Convert",command=converter)
button.place(x=90,y=117)
window=mainloop()