import tkinter

window = tkinter.Tk()

label= tkinter.Label(window,text='probando',bg='green',fg='red')
label2= tkinter.Label(window,text='probando',bg='blue',fg='red')
label3= tkinter.Label(window,text='label3',bg='purple',fg='red')
label4= tkinter.Label(window,text='label4',bg='red',fg='green')
label5= tkinter.Label(window,text='label5',bg='gray',fg='green')
label6= tkinter.Label(window,text='label6',bg='pink',fg='green')
label.pack(ipadx=50, ipady=50, fill='both') 
label2.pack(ipadx=50, ipady=50, fill='both')
label3.pack(ipadx=50, ipady=50, fill='both') 
label4.pack(side='left',ipadx=50, ipady=50, fill='both') 
label5.pack(side='left',ipadx=50, ipady=50, fill='both')
label6.pack(side='right',ipadx=50, ipady=50, fill='both')

window.mainloop()