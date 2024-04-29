from tkinter import *

login = Tk()
login.title("Login SGDC")
login.resizable(False, False)
login.iconbitmap("imagens/icon.ico")

largura_janela = 700 
altura_janela = 500 

largura_tela = login.winfo_screenwidth()
altura_tela = login.winfo_screenheight()

posx = (largura_tela - largura_janela) // 2
posy = (altura_tela - altura_janela) // 2

login.geometry("%dx%d+%d+%d" % (largura_janela, altura_janela, posx, posy))

login = Label(login, text="login")
login.grid(column=1, row=1, padx=10, pady=10)

email = Label(login, text="Seu e-mail")
email.grid(column=0, row=3, padx=10, pady=10)
emailentry = Entry(login)
emailentry.grid(column=0, row=4, padx=10, pady=10)

senha = Label(login, text="Sua senha")
senha.grid(column=0, row=5, padx=10, pady=10)
senhaentry = Entry(login)
senhaentry.grid(column=0, row=6, padx=10, pady=10)

manter_logado_var = BooleanVar()
manter_logado_checkbox = Checkbutton(login, text="Manter Logado", variable=manter_logado_var)
manter_logado_checkbox.grid(column=0, row=7, padx=10, pady=10)

logar = Button(login, text="Logar", command='logar_cliente')
logar.grid(column=1, row=8, padx=10, pady=10)

login.mainloop()