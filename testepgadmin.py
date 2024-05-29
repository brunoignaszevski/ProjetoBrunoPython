from tkinter import *
from tkinter import messagebox
import psycopg2

contador_clientes = 0
codigos_utilizados = set()
clientes = []

def conectar_banco():
    return psycopg2.connect(
        dbname="sistema_gerenciador_de_clientes",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    posx = (largura_tela - largura) // 2
    posy = (altura_tela - altura) // 2
    janela.geometry(f"{largura}x{altura}+{posx}+{posy}")

def verificar_login():
    email_digitado = emailentry.get()
    senha_digitada = senhaentry.get()
    email_valido = "bruno@gmail.com"
    senha_valida = "123456"

    if email_digitado == email_valido and senha_digitada == senha_valida:
        login.destroy()
        abrir_menu_principal()
    else:
        messagebox.showerror("Login", "Credenciais inválidas!")

def abrir_menu_principal():
    menu_principal = Tk()
    menu_principal.title("Sistema Gerenciador de Clientes")
    menu_principal.resizable(False, False)
    menu_principal.iconbitmap("imagens/icon.ico")
    centralizar_janela(menu_principal, 700, 500)
    
    botao_cadastro = Button(menu_principal, text="Cadastro de clientes", command=abrir_tela_cadastro)
    botao_cadastro.pack()    
    botao_cadastro.place(x=0, y=0) 
    botao_editar = Button(menu_principal, text="Editar clientes", command=abrir_editar_clientes)
    botao_editar.pack()
    botao_editar.place(x=118, y=0)
    botao_excluir = Button(menu_principal, text="Excluir clientes", command=abrir_excluir_clientes)
    botao_excluir.pack()
    botao_excluir.place(x=202, y=0)

def abrir_excluir_clientes():
    excluir = Toplevel()
    excluir.title("Excluir Clientes")
    excluir.resizable(False, False)
    excluir.iconbitmap("imagens/icon.ico")
    centralizar_janela(excluir, 700, 500)

    listbox = Listbox(excluir, width=100, height=20)
    listbox.pack(pady=20)
    
    global clientes
    clientes = ler_clientes()
    for idx, cliente in enumerate(clientes):
        nome = cliente.get("Nome", "")
        sobrenome = cliente.get("Sobrenome", "")
        listbox.insert(END, f"{idx + 1}: {nome} {sobrenome}")

    def excluir_cliente():
        selection = listbox.curselection()
        if not selection:
            messagebox.showerror("Erro", "Selecione um cliente para excluir.")
            return
        index = selection[0]
        cliente = clientes[index]

        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM clientes WHERE codigo = %s", (cliente["Codigo"],))
        conexao.commit()
        cursor.close()
        conexao.close()

        clientes.pop(index)
        listbox.delete(index)

        messagebox.showinfo("Sucesso", "Cliente excluído com sucesso.")

    botao_excluir = Button(excluir, text="Excluir Cliente", command=excluir_cliente)
    botao_excluir.pack(pady=10)

def abrir_editar_clientes():
    editar = Toplevel()
    editar.title("Editar Clientes")
    editar.resizable(False, False)
    editar.iconbitmap("imagens/icon.ico")
    centralizar_janela(editar, 700, 500)

    listbox = Listbox(editar, width=100, height=20)
    listbox.pack(pady=20)
    
    global clientes
    clientes = ler_clientes()
    for idx, cliente in enumerate(clientes):
        nome = cliente.get("Nome", "")
        sobrenome = cliente.get("Sobrenome", "")
        listbox.insert(END, f"{idx + 1}: {nome} {sobrenome}")

    def carregar_dados_cliente():
        selection = listbox.curselection()
        if not selection:
            messagebox.showerror("Erro", "Selecione um cliente para editar.")
            return
        index = selection[0]
        cliente = clientes[index]
        abrir_tela_cadastro(cliente, index)

    botao_carregar = Button(editar, text="Carregar Cliente", command=carregar_dados_cliente)
    botao_carregar.pack(pady=10)

def abrir_tela_cadastro(cliente=None, index=None):
    global contador_clientes, clientes
    cadastro = Toplevel()
    cadastro.title("Cadastro de Clientes")
    
    def cadastrar_cliente():
        global contador_clientes, clientes
        nome = nomeentry.get()
        sobrenome = sobrenomeentry.get()
        nascimento = nascimentoentry.get()
        genero = generoentry.get()
        endereco = enderecoentry.get()
        numero = numeroentry.get()
        numerotelefone = numerotelefoneentry.get()
        email = emailentry.get()
        codigo_cliente = gerar_codigo() if cliente is None else cliente["Codigo"]

        cliente_novo = {
            "Codigo": codigo_cliente,
            "Nome": nome,
            "Sobrenome": sobrenome,
            "Nascimento": nascimento,
            "Genero": genero,
            "Endereco": endereco,
            "Numero": numero,
            "NumeroTelefone": numerotelefone,
            "Email": email
        }

        conexao = conectar_banco()
        cursor = conexao.cursor()
        if cliente is None:
            cursor.execute("""
                INSERT INTO clientes (codigo, nome, sobrenome, nascimento, genero, endereco, numero, numerotelefone, email)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                codigo_cliente,
                nome,
                sobrenome,
                nascimento,
                genero,
                endereco,
                numero,
                numerotelefone,
                email
            ))
            clientes.append(cliente_novo)
        else:
            cursor.execute("""
                UPDATE clientes
                SET nome = %s, sobrenome = %s, nascimento = %s, genero = %s, endereco = %s, numero = %s, numerotelefone = %s, email = %s
                WHERE codigo = %s
            """, (
                nome,
                sobrenome,
                nascimento,
                genero,
                endereco,
                numero,
                numerotelefone,
                email,
                codigo_cliente
            ))
            clientes[index] = cliente_novo
        conexao.commit()
        cursor.close()
        conexao.close()

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
        contador_clientes += 1
        escrever_contador(contador_clientes)
        return contador_clientes

    cadastro.geometry("300x500")
    cadastro.resizable(False, False)
    cadastro.iconbitmap("imagens/icon.ico")
    centralizar_janela(cadastro, 700, 500)

    Label(cadastro, text="Nome").grid(column=0, row=1, padx=10, pady=10)
    nomeentry = Entry(cadastro)
    nomeentry.grid(column=0, row=2, padx=10, pady=10)

    Label(cadastro, text="Sobrenome").grid(column=1, row=1)
    sobrenomeentry = Entry(cadastro)
    sobrenomeentry.grid(column=1, row=2)

    Label(cadastro, text="Data de nascimento").grid(column=0, row=3, padx=10, pady=10)
    nascimentoentry = Entry(cadastro)
    nascimentoentry.grid(column=0, row=4, padx=10, pady=10)

    Label(cadastro, text="Gênero").grid(column=1, row=3)
    generoentry = Entry(cadastro)
    generoentry.grid(column=1, row=4)

    Label(cadastro, text="Endereço").grid(column=0, row=5, padx=10, pady=10)
    enderecoentry = Entry(cadastro)
    enderecoentry.grid(column=0, row=6, padx=10, pady=10)

    Label(cadastro, text="Número").grid(column=1, row=5)
    numeroentry = Entry(cadastro)
    numeroentry.grid(column=1, row=6)

    Label(cadastro, text="Número de telefone").grid(column=0, row=7, padx=10, pady=10)
    numerotelefoneentry = Entry(cadastro)
    numerotelefoneentry.grid(column=0, row=8, padx=10, pady=10)

    Label(cadastro, text="E-mail").grid(column=1, row=7)
    emailentry = Entry(cadastro)
    emailentry.grid(column=1, row=8)

    botao_cadastrar = Button(cadastro, text="Cadastrar cliente", command=cadastrar_cliente)
    botao_cadastrar.grid(column=0, row=9, columnspan=2, padx=10, pady=10)

    if cliente is not None:
        nomeentry.insert(0, cliente["Nome"])
        sobrenomeentry.insert(0, cliente["Sobrenome"])
        nascimentoentry.insert(0, cliente["Nascimento"])
        generoentry.insert(0, cliente["Genero"])
        enderecoentry.insert(0, cliente["Endereco"])
        numeroentry.insert(0, cliente["Numero"])
        numerotelefoneentry.insert(0, cliente["NumeroTelefone"])
        emailentry.insert(0, cliente["Email"])

def ler_clientes():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT codigo, nome, sobrenome, nascimento, genero, endereco, numero, numerotelefone, email FROM clientes")
    clientes = []
    for row in cursor.fetchall():
        cliente = {
            "Codigo": row[0],
            "Nome": row[1],
            "Sobrenome": row[2],
            "Nascimento": row[3],
            "Genero": row[4],
            "Endereco": row[5],
            "Numero": row[6],
            "NumeroTelefone": row[7],
            "Email": row[8]
        }
        clientes.append(cliente)
    cursor.close()
    conexao.close()
    return clientes

def salvar_clientes(lista_de_clientes):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute("DELETE FROM clientes")
    
    for cliente in lista_de_clientes:
        cursor.execute("""
            INSERT INTO clientes (codigo, nome, sobrenome, nascimento, genero, endereco, numero, numerotelefone, email)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            cliente["Codigo"],
            cliente["Nome"],
            cliente["Sobrenome"],
            cliente["Nascimento"],
            cliente["Genero"],
            cliente["Endereco"],
            cliente["Numero"],
            cliente["NumeroTelefone"],
            cliente["Email"]
        ))
    conexao.commit()
    cursor.close()
    conexao.close()

login = Tk()
login.title("Login SGDC")
login.resizable(False, False)
login.iconbitmap("imagens/icon.ico")
centralizar_janela(login, 700, 500)

Label(login, text="Seu e-mail").place(relx=0.5, rely=0.4, anchor="center")
emailentry = Entry(login, width=40)
emailentry.place(relx=0.5, rely=0.45, anchor="center")

Label(login, text="Sua senha").place(relx=0.5, rely=0.5, anchor="center")
senhaentry = Entry(login, width=40, show="*")
senhaentry.place(relx=0.5, rely=0.55, anchor="center")

Button(login, text="Logar", command=verificar_login, width=30).place(relx=0.5, rely=0.65, anchor="center")

login.mainloop()
