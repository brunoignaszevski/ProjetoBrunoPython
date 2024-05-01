from tkinter import *

def abrir_tela_cadastro():
    cadastro = Toplevel()
    cadastro.title("Cadastro de Clientes")

    def abrir_cadastro():
        Toplevel(cadastro)

    def ler_contador():
        try:
            with open("contador.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 1

    def escrever_contador(valor):
        with open("contador.txt", "w") as file:
            file.write(str(valor))

    def gerar_codigo():
        global contador_clientes
        while True:
            if contador_clientes not in codigos_utilizados:
                codigo = contador_clientes
                contador_clientes += 1
                return codigo
            else:
                contador_clientes += 1

    def cadastrar_cliente():
        global contador_clientes
        nome = nomeentry.get()
        sobrenome = sobrenomeentry.get()
        nascimento = nascimentoentry.get()
        genero = generoentry.get()
        endereco = enderecoentry.get()
        numero = numeroentry.get()
        numerotelefone = numerotelefoneentry.get()
        email = emailentry.get()
        codigo_cliente = gerar_codigo()
        codigos_utilizados.add(codigo_cliente)

        with open("clientes.txt", "a") as file:
            file.write(f"Código: {codigo_cliente}\n")
            file.write(f"Nome: {nome}\n")
            file.write(f"Sobrenome: {sobrenome}\n")
            file.write(f"Idade: {nascimento}\n")
            file.write(f"Gênero: {genero}\n")
            file.write(f"Endereço: {endereco}\n")
            file.write(f"Número: {numero}\n")
            file.write(f"Número de telefone: {numerotelefone}\n")
            file.write(f"Endereço de e-mail: {email}\n")
            file.write("\n") 

        nomeentry.delete(0, END)
        sobrenomeentry.delete(0, END)
        nascimentoentry.delete(0, END)
        generoentry.delete(0, END)
        enderecoentry.delete(0, END)
        numeroentry.delete(0, END)
        numerotelefoneentry.delete(0, END)
        emailentry.delete(0, END)

        escrever_contador(contador_clientes)

    titulo = Label(cadastro, text="Cadastro de Clientes")
    titulo.grid(column=0, row=0, padx=10, pady=10)
    cadastro.geometry("300x500")
    cadastro.resizable(False, False)
    cadastro.iconbitmap("imagens/icon.ico")

    largura_janela = 700 
    altura_janela = 500 

    largura_tela = cadastro.winfo_screenwidth()
    altura_tela = cadastro.winfo_screenheight()

    posx = (largura_tela - largura_janela) // 2
    posy = (altura_tela - altura_janela) // 2

    cadastro.geometry("%dx%d+%d+%d" % (largura_janela, altura_janela, posx, posy))

    nome = Label(cadastro, text="Nome")
    nome.grid(column=0, row=1, padx=10, pady=10)
    nomeentry = Entry(cadastro)
    nomeentry.grid(column=0, row=2, padx=10, pady=10)

    sobrenome = Label(cadastro, text="Sobrenome")
    sobrenome.grid(column=1, row=1)
    sobrenomeentry = Entry(cadastro)
    sobrenomeentry.grid(column=1, row=2)

    nascimento = Label(cadastro, text="Data de nascimento")
    nascimento.grid(column=0, row=3, padx=10, pady=10)
    nascimentoentry = Entry(cadastro)
    nascimentoentry.grid(column=0, row=4, padx=10, pady=10)

    genero = Label(cadastro, text="Gênero")
    genero.grid(column=1, row=3)
    generoentry = Entry(cadastro)
    generoentry.grid(column=1, row=4)

    endereco = Label(cadastro, text="Endereço")
    endereco.grid(column=0, row=5, padx=10, pady=10)
    enderecoentry = Entry(cadastro)
    enderecoentry.grid(column=0, row=6, padx=10, pady=10)

    numero = Label(cadastro, text="Número")
    numero.grid(column=1, row=5)
    numeroentry = Entry(cadastro)
    numeroentry.grid(column=1, row=6)

    numerotelefone = Label(cadastro, text="Número de telefone")
    numerotelefone.grid(column=0, row=7, padx=10, pady=10)
    numerotelefoneentry = Entry(cadastro)
    numerotelefoneentry.grid(column=0, row=8, padx=10, pady=10)

    email = Label(cadastro, text="Endereço de e-mail")
    email.grid(column=0, row=9, padx=10, pady=10)
    emailentry = Entry(cadastro)
    emailentry.grid(column=0, row=10, padx=10, pady=10)

    cadastrar = Button(cadastro, text="Cadastrar", command=cadastrar_cliente, width=30)
    cadastrar.grid(column=1, row=11, padx=10, pady=10)

    contador_clientes = ler_contador()
    codigos_utilizados = set()

    cadastro.mainloop()

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

botao_cadastro = Button(menu_principal, text="Cadastro de clientes", command=abrir_tela_cadastro)
botao_cadastro.pack()

menu_principal.mainloop()
