#pip install requests
import requests
from tkinter import *

def cadastrar_clientes():
    nome = nomeentry.get()
    sobrenome = sobrenomeentry.get()
    idade = idadeentry.get()
    genero = generoentry.get()
    endereco = enderecoentry.get()
    numero = numeroentry.get()
    numerotelefone = numerotelefoneentry.get()
    email = emailentry.get()

    print("Nome:", nome)
    print("Sobrenome:", sobrenome)
    print("Idade:", idade)
    print("Gênero:", genero)
    print("Endereço:", endereco)
    print("Número:", numero)
    print("Número de telefone:", numerotelefone)
    print("Endereço de e-mail:", email)

janela = Tk()
janela.title("Cadastro de Clientes")
titulo = Label(janela, text="Cadastro de Clientes")
titulo.grid(column=0, row=0, padx=10, pady=10)

nome = Label(janela, text="Nome")
nome.grid(column=0, row=1, padx=10, pady=10)
nomeentry = Entry(janela)
nomeentry.grid(column=0, row=2, padx=10, pady=10)

sobrenome = Label(janela, text="Sobrenome")
sobrenome.grid(column=1, row=1)
sobrenomeentry = Entry(janela)
sobrenomeentry.grid(column=1, row=2)

idade = Label(janela, text="Idade")
idade.grid(column=0, row=3, padx=10, pady=10)
idadeentry = Entry(janela)
idadeentry.grid(column=0, row=4, padx=10, pady=10)

genero = Label(janela, text="Gênero")
genero.grid(column=1, row=3)
generoentry = Entry(janela)
generoentry.grid(column=1, row=4)

endereco = Label(janela, text="Endereço")
endereco.grid(column=0, row=5, padx=10, pady=10)
enderecoentry = Entry(janela)
enderecoentry.grid(column=0, row=6, padx=10, pady=10)

numero = Label(janela, text="Número")
numero.grid(column=1, row=5)
numeroentry = Entry(janela)
numeroentry.grid(column=1, row=6)

numerotelefone = Label(janela, text="Número de telefone")
numerotelefone.grid(column=0, row=7, padx=10, pady=10)
numerotelefoneentry = Entry(janela)
numerotelefoneentry.grid(column=0, row=8, padx=10, pady=10)

email = Label(janela, text="Endereço de e-mail")
email.grid(column=0, row=9, padx=10, pady=10)
emailentry = Entry(janela)
emailentry.grid(column=0, row=10, padx=10, pady=10)

botao = Button(janela, text="Cadastrar", command=cadastrar_clientes)
botao.grid(column=0, row=11, padx=10, pady=10)
janela.mainloop()



