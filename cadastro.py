from tkinter import *

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
    idade = idadeentry.get()
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
        file.write(f"Idade: {idade}\n")
        file.write(f"Gênero: {genero}\n")
        file.write(f"Endereço: {endereco}\n")
        file.write(f"Número: {numero}\n")
        file.write(f"Número de telefone: {numerotelefone}\n")
        file.write(f"Endereço de e-mail: {email}\n")
        file.write("\n") 

    nomeentry.delete(0, END)
    sobrenomeentry.delete(0, END)
    idadeentry.delete(0, END)
    generoentry.delete(0, END)
    enderecoentry.delete(0, END)
    numeroentry.delete(0, END)
    numerotelefoneentry.delete(0, END)
    emailentry.delete(0, END)

    escrever_contador(contador_clientes)

janela2 = Tk()
janela2.title("Cadastro de Clientes")
titulo = Label(janela2, text="Cadastro de Clientes")
titulo.grid(column=0, row=0, padx=10, pady=10)

nome = Label(janela2, text="Nome")
nome.grid(column=0, row=1, padx=10, pady=10)
nomeentry = Entry(janela2)
nomeentry.grid(column=0, row=2, padx=10, pady=10)

sobrenome = Label(janela2, text="Sobrenome")
sobrenome.grid(column=1, row=1)
sobrenomeentry = Entry(janela2)
sobrenomeentry.grid(column=1, row=2)

idade = Label(janela2, text="Idade")
idade.grid(column=0, row=3, padx=10, pady=10)
idadeentry = Entry(janela2)
idadeentry.grid(column=0, row=4, padx=10, pady=10)

genero = Label(janela2, text="Gênero")
genero.grid(column=1, row=3)
generoentry = Entry(janela2)
generoentry.grid(column=1, row=4)

endereco = Label(janela2, text="Endereço")
endereco.grid(column=0, row=5, padx=10, pady=10)
enderecoentry = Entry(janela2)
enderecoentry.grid(column=0, row=6, padx=10, pady=10)

numero = Label(janela2, text="Número")
numero.grid(column=1, row=5)
numeroentry = Entry(janela2)
numeroentry.grid(column=1, row=6)

numerotelefone = Label(janela2, text="Número de telefone")
numerotelefone.grid(column=0, row=7, padx=10, pady=10)
numerotelefoneentry = Entry(janela2)
numerotelefoneentry.grid(column=0, row=8, padx=10, pady=10)

email = Label(janela2, text="Endereço de e-mail")
email.grid(column=0, row=9, padx=10, pady=10)
emailentry = Entry(janela2)
emailentry.grid(column=0, row=10, padx=10, pady=10)

botao = Button(janela2, text="Cadastrar", command=cadastrar_cliente)
botao.grid(column=0, row=11, padx=10, pady=10)

contador_clientes = ler_contador()
codigos_utilizados = set()

janela2.mainloop()
