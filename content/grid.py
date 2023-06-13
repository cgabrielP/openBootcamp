import tkinter
from tkinter import ttk

window=tkinter.Tk()
def saludar(e):
    print('Han clicado')
def salir(e):
    print('Bye')
    window.quit()
lista_nums=[1,2,3,4,5,6,7,8,9]
lista_nums_ver=tkinter.StringVar(value=lista_nums)
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

listbox = tkinter.Listbox(window,justify='center', listvariable=lista_nums_ver)
listbox.grid(column=1,row=4,sticky=tkinter.W)

selected=tkinter.StringVar()
radio_button= ttk.Radiobutton(window, text='Si',  variable=selected)
# radio_button.grid(column=0, row=4)
boton=ttk.Button(window,text='Click')
boton.bind('<Button-1>',saludar)
boton.grid(column=0, row=4)

boton_salir=ttk.Button(window,text='Salir')
boton_salir.bind('<Button-1>',salir)
boton_salir.grid(column=0, row=5)



username_label=ttk.Label(window, text='Usuario: ')
username_label.grid(column=0,row=0,sticky=tkinter.W, padx=5,pady=5)

username_input=ttk.Entry(window)
username_input.grid(column=1,row=0,sticky=tkinter.E, padx=5,pady=5)

password_label=ttk.Label(window, text='Contraseña: ')
password_label.grid(column=0,row=1,sticky=tkinter.W, padx=5,pady=5)

password_input=ttk.Entry(window,show='*')
password_input.grid(column=1,row=1,sticky=tkinter.E, padx=5,pady=5)

login_button=ttk.Button(window,text='Login')
login_button.grid(column=1,row=3,sticky=tkinter.E)



window.mainloop()