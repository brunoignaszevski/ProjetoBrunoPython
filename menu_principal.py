from tkinter import *
from cadastro import *

menu_principal = Tk()
menu_principal.title("Sistema Gerenciador de Clientes")
menu_principal.resizable(False, False)
menu_principal.iconbitmap("imagens/icon.ico")

largura_janela = 700 
altura_janela = 500 

largura_tela = menu_principal.winfo_screenwidth()
altura_tela = menu_principal.winfo_screenheight()

posx = (largura_tela - largura_janela) // 2
posy = (altura_tela - altura_janela) // 2

menu_principal.geometry("%dx%d+%d+%d" % (largura_janela, altura_janela, posx, posy))

botao_cadastro = Button(menu_principal, text="Cadastro de clientes", command=cadastro)
botao_cadastro.pack()

menu_principal.mainloop()