import tkinter as tk

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
    # Verifica se o código já foi usado antes
    while True:
        if contador_clientes not in codigos_utilizados:
            codigo = contador_clientes
            contador_clientes += 1
            return codigo
        else:
            contador_clientes += 1

def cadastrar_cliente():
    global contador_clientes
    # Obtém todas as informações digitadas nos campos de entrada
    nome = nomeentry.get()
    sobrenome = sobrenomeentry.get()
    idade = idadeentry.get()
    genero = generoentry.get()
    endereco = enderecoentry.get()
    numero = numeroentry.get()
    numerotelefone = numerotelefoneentry.get()
    email = emailentry.get()

    # Gera um código único para o cliente
    codigo_cliente = gerar_codigo()
    codigos_utilizados.add(codigo_cliente)

    # Salva as informações em um arquivo de texto
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
        file.write("\n")  # Adiciona uma linha em branco entre os registros

    # Limpa todos os campos de entrada
    nomeentry.delete(0, tk.END)
    sobrenomeentry.delete(0, tk.END)
    idadeentry.delete(0, tk.END)
    generoentry.delete(0, tk.END)
    enderecoentry.delete(0, tk.END)
    numeroentry.delete(0, tk.END)
    numerotelefoneentry.delete(0, tk.END)
    emailentry.delete(0, tk.END)

    # Atualiza o contador e o salva
    escrever_contador(contador_clientes)

janela = tk.Tk()
janela.title("Cadastro de Clientes")
titulo = tk.Label(janela, text="Cadastro de Clientes")
titulo.grid(column=0, row=0, padx=10, pady=10)

nome = tk.Label(janela, text="Nome")
nome.grid(column=0, row=1, padx=10, pady=10)
nomeentry = tk.Entry(janela)
nomeentry.grid(column=0, row=2, padx=10, pady=10)

sobrenome = tk.Label(janela, text="Sobrenome")
sobrenome.grid(column=1, row=1)
sobrenomeentry = tk.Entry(janela)
sobrenomeentry.grid(column=1, row=2)

idade = tk.Label(janela, text="Idade")
idade.grid(column=0, row=3, padx=10, pady=10)
idadeentry = tk.Entry(janela)
idadeentry.grid(column=0, row=4, padx=10, pady=10)

genero = tk.Label(janela, text="Gênero")
genero.grid(column=1, row=3)
generoentry = tk.Entry(janela)
generoentry.grid(column=1, row=4)

endereco = tk.Label(janela, text="Endereço")
endereco.grid(column=0, row=5, padx=10, pady=10)
enderecoentry = tk.Entry(janela)
enderecoentry.grid(column=0, row=6, padx=10, pady=10)

numero = tk.Label(janela, text="Número")
numero.grid(column=1, row=5)
numeroentry = tk.Entry(janela)
numeroentry.grid(column=1, row=6)

numerotelefone = tk.Label(janela, text="Número de telefone")
numerotelefone.grid(column=0, row=7, padx=10, pady=10)
numerotelefoneentry = tk.Entry(janela)
numerotelefoneentry.grid(column=0, row=8, padx=10, pady=10)

email = tk.Label(janela, text="Endereço de e-mail")
email.grid(column=0, row=9, padx=10, pady=10)
emailentry = tk.Entry(janela)
emailentry.grid(column=0, row=10, padx=10, pady=10)

# Define a função para ser chamada quando o botão for clicado
botao = tk.Button(janela, text="Cadastrar", command=cadastrar_cliente)
botao.grid(column=0, row=11, padx=10, pady=10)

# Inicializa o contador de clientes e os códigos utilizados
contador_clientes = ler_contador()
codigos_utilizados = set()

janela.mainloop()
