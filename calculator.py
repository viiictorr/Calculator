from tkinter import *


win = Tk()  # Creamos la ventana básica
win.geometry("312x324")  # Definimos el tamaño de la ventana
win.resizable(0, 0)  # Impedimos cambiar la resolución
win.title("Calculadora")

# Actualizamos cada vez que escribamos un numero


def click_boton(objeto):
    global expression
    expression = expression + str(objeto)
    input_text.set(expression)

# Definimos el boton para borrar las expresiones


def boton_eliminar():
    global expression
    expression = ""
    input_text.set("")

# Definimos el boton de igual


def boton_igual():
    global expression
    resultado = str(eval(expression))
    input_text.set(resultado)
    expression = ""


expression = ""

input_text = StringVar()  # Se usa para conseguir la entrada

# Creamos la casilla para introducir cosas

input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightbackground="black", highlightthickness=2)

input_frame.pack(side=TOP)

# Enesñamos lo escrito en el cuadro

input_field = Entry(input_field, font=("Dura Sans", 20, "bold"),
                    textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)

# Creamos otro cuadro debajo de los anteriores para introducir un boton

marco_botones = Frame(win, widht=312, height=272.5, bg="grey")

marco_botones.pack()

# Primera fila

borrar = Button(marco_botones, text="C", fg="black", width=32, height=3, bd=0, bg="#eee",
                cursor="hand2", command=lambda: boton_eliminar()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

dividir = Button(marco_botones, text="C", fg="black", width=32, height=3, bd=0, bg="#eee",
                 cursor="hand2", command=lambda: click_boton("/")).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

win.mainloop()
