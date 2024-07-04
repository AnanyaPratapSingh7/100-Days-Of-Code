from tkinter import *

window = Tk()
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)
def convert():
    miles = int(entry.get())
    answer = miles*1.609344
    label_answer.config(text=answer)
    

entry = Entry(width=15)
entry.insert(END, "0")

label_miles = Label(text="Miles")
label_is_equal_to = Label(text="is equal to")
label_answer = Label(text=0)
label_km = Label(text="Km")
button = Button(text="Calculate", command=convert)

entry.grid(row=0, column=1)
label_miles.grid(row=0, column=2)
label_is_equal_to.grid(row=1, column=0)
label_answer.grid(row=1, column=1)
label_km.grid(row=1, column=2)
button.grid(row=2, column=1)

window.mainloop()