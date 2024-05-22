"""
    excluir.geometry("300x500")
    excluir.resizable(False, False)
    excluir.iconbitmap("imagens/icon.ico")
    largura_janela = 700 
    altura_janela = 500 
    largura_tela = excluir.winfo_screenwidth()
    altura_tela = excluir.winfo_screenheight()
    posx = (largura_tela - largura_janela) // 2
    posy = (altura_tela - altura_janela) // 2
    excluir.geometry("%dx%d+%d+%d" % (largura_janela, altura_janela, posx, posy))

    titulo = Label(excluir, text="Excluir Clientes")
    titulo.grid(column=0, row=0, padx=10, pady=10)
"""