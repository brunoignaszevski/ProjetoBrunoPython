#importações de módulos 
from tkinter import *
from tkinter import messagebox
#zerando contador
contador_clientes = 0
codigos_utilizados = set()

def verificar_login():
    email_digitado = emailentry.get()
    senha_digitada = senhaentry.get()
    #verificar os dados de login em algum lugar seguro ex: banco de dados
    email_valido = "bruno@gmail.com"
    senha_valida = "123456"

    if email_digitado == email_valido and senha_digitada == senha_valida:
        login.destroy()
        abrir_menu_principal()
    else:
        messagebox.showerror("Login", "Credenciais inválidas!")

def abrir_menu_principal():
    menu_principal = Toplevel()
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

def abrir_tela_cadastro():
    cadastro = Toplevel()
    cadastro.title("Cadastro de Clientes")

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
        codigo = contador_clientes
        contador_clientes += 1
        return codigo

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

    titulo = Label(cadastro, text="Cadastro de Clientes")
    titulo.grid(column=0, row=0, padx=10, pady=10)

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

login = Tk()
login.title("Login SGDC")
login.resizable(False, False)
login.iconbitmap("imagens/icon.ico")

def ocultar_senha(event=None):
    senhaentry.config(show="*")

largura_janela = 700 
altura_janela = 500 
largura_tela = login.winfo_screenwidth()
altura_tela = login.winfo_screenheight()
posx = (largura_tela - largura_janela) // 2
posy = (altura_tela - altura_janela) // 2
login.geometry("%dx%d+%d+%d" % (largura_janela, altura_janela, posx, posy))

email = Label(login, text="Seu e-mail")
email.place(relx=0.5, rely=0.4, anchor="center")
emailentry = Entry(login, width=40)
emailentry.place(relx=0.5, rely=0.45, anchor="center")

senha = Label(login, text="Sua senha")
senha.place(relx=0.5, rely=0.5, anchor="center")
senhaentry = Entry(login, width=40)
senhaentry.place(relx=0.5, rely=0.55, anchor="center")
senhaentry.bind("<FocusIn>", ocultar_senha)

# Botão de login
logar = Button(login, text="Logar", command=verificar_login, width=30)
logar.place(relx=0.5, rely=0.65, anchor="center")

login.mainloop()
