from tkinter import *

def mostrarNome():
    nome = textbox_1.get()
    label_final = Label(root, text="O teu nome é "+nome)
    label_final.grid()


# Interface Gráfica
root = Tk()
root.title("Escreva seu nome")
root.geometry("200x100")

# Onde o nome é escrito
label_1 = Label(root,text="Escreve o teu nome: ")
textbox_1 = Entry(root)
button_1 = Button(root, text="Executar", command=mostrarNome)

label_1.grid()
textbox_1.grid()
button_1.grid()

root.mainloop()