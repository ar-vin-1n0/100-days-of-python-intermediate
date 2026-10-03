import tkinter

window = tkinter.Tk()

window.title("Gui shit")
window.minsize(500, 300)
window.config(padx=100,pady=100)



def on_button_click():
    conversion_factor = 0.621371
    miles = float(km_entry.get()) * conversion_factor
    a_label = tkinter.Label(text=miles,font=("Arial",25))
    a_label.grid(row=1,column=1)
    label.config(padx=20, pady=20)

label = tkinter.Label(text="is equal to",font=("Arial",25))
label.grid(row=1,column=0)
label.config(padx=20,pady=20)

km_entry = tkinter.Entry(width=10,font=("Arial",25))
km_entry.grid(row=0,column=1)

label = tkinter.Label(text="km",font=("Arial",25))
label.grid(row=0,column=2)
label.config(padx=20,pady=20)

button = tkinter.Button(text="Calculate",command=on_button_click,font=("Arial",20))
button.grid(row=2,column=1)

label = tkinter.Label(text="miles",font=("Arial",25))
label.grid(row=1,column=2)
label.config(padx=20,pady=20)
window.mainloop()