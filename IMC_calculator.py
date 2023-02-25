from tkinter import *
from tkinter import ttk


def calculate():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    
    imc = round(weight / (height**2), 1)
    result = " "
    if imc < 18.5 and imc > 0:
        result = "O seu IMC está abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        result = "O seu IMC está no peso normal"
    elif imc >= 25 and imc < 30:
        result = "O seu IMC está no sobrepeso"
    else:
        result = "O seu IMC está na obesidade"
    
    if imc < 0:
        result = "Erro! O peso só pode ser positivo"
        imc = "ERROR"
        imc_text['fg'] = red
        imc_result['fg'] = red
    else:
        imc_text['fg'] = white
        imc_result['fg'] = purple
        
    imc_text["text"] = str(imc)
    imc_result["text"] = str(result)


# Colors
white = "#eaede8"
black = "#050505"
purple = "#2b0075"
red = "#fc031c"

# Window
window = Tk()
window.geometry("400x260")
window.maxsize(400, 260)
window.minsize(400, 260)

# Frames
title_zone = Frame(window, width=400, height=60, bg=purple)
title_zone.grid(row=0, column=0)

interative_zone = Frame(window, width=400, height=200, bg=white)
interative_zone.grid(row=1, column=0)

# Labels
app_name = Label(title_zone, text="Calculadora de IMC", relief="flat",
                 height=2, width=23, font=('Ivy 20 bold'), 
                 anchor="center", fg=white, bg=purple)
app_name.place(x=0, y=0)

weight_text = Label(interative_zone, text="Peso (kg)", font=('Ivy 14 bold'), 
                    relief="flat", bg=white, fg=black)
weight_text.place(x=10, y=20)

height_text = Label(interative_zone, text="Altura (m)", font=("Ivy 14 bold"),
                    relief="flat", bg=white, fg=black)
height_text.place(x=10, y=50)

imc_text = Label(interative_zone, text="- - - - -", width=10,
                 font=('Ivy 25 bold'), pady=6, bg=purple, fg=white)
imc_text.place(x=180, y=24)

imc_result = Label(interative_zone, text=" ",
                   width=36, bg=white, fg=purple, 
                   font=('Ivy 14'), anchor="center")
imc_result.place(x=0, y=100)

# Entry
weight_entry = Entry(interative_zone, width=6, font=('Ivy 13 bold'),
                     relief=SOLID)
weight_entry.place(x=110, y=24)

height_entry = Entry(interative_zone, width=6, font=('Ivy 13 bold'),
                     relief=SOLID)
height_entry.place(x=110, y=54)

# Button
button_calculate = Button(interative_zone, text="Calcular", font=("Ivy 12 bold"),
                          width=37, relief=RAISED, fg=white, bg=purple,
                          overrelief=RIDGE, activeforeground=white, 
                          activebackground=purple, command=calculate)
button_calculate.place(x=10, y=150)

window.mainloop()
