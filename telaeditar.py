"""
    editar.geometry("300x500")
    editar.resizable(False, False)
    editar.iconbitmap("imagens/icon.ico")
    largura_janela = 700 
    altura_janela = 500 
    largura_tela = editar.winfo_screenwidth()
    altura_tela = editar.winfo_screenheight()
    posx = (largura_tela - largura_janela) // 2
    posy = (altura_tela - altura_janela) // 2
    editar.geometry("%dx%d+%d+%d" % (largura_janela, altura_janela, posx, posy))

    titulo = Label(editar, text="Editar Clientes")
    titulo.grid(column=0, row=0, padx=10, pady=10)
"""