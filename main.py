from tkinter import *


def calculate():
    miles_entry = str(float(miles.get()) * 1.609)
    label3["text"] = miles_entry


# Screen
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=70, pady=20)

# Input miles
miles = Entry(width=10)
miles.grid(row=0, column=1)

# Label 1
label1 = Label(text="Miles")
label1.grid(row=0, column=2)

# Label 2
label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

# Label 3
label3 = Label(text="0")
label3.grid(row=1, column=1)

# Label 4
label4 = Label(text="Km")
label4.grid(row=1, column=2)

# Calculate button
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

window.mainloop()
