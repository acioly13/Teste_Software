from tkinter import *
from tkinter import ttk


# CADASTRAR ALUNO
def nova_janela_cadastrar_aluno():
    nova_janela_cadastrar_aluno = Toplevel()
    nova_janela_cadastrar_aluno.title("Cadastrar Aluno")
    nova_janela_cadastrar_aluno.geometry("190x200")
    nova_janela_cadastrar_aluno.resizable(False, False)

    botao_inserir_aluno = Button(nova_janela_cadastrar_aluno, text="Inserir Aluno", command=nova_janela_inserir_aluno)
    botao_inserir_aluno.grid(column=0, row=1, padx=50, pady=20)
    botao_excluir_aluno = Button(nova_janela_cadastrar_aluno, text="Excluir Aluno", command=nova_janela_excluir_aluno)
    botao_excluir_aluno.grid(column=0, row=2, padx=50)
    botao_buscar_aluno = Button(nova_janela_cadastrar_aluno, text="Buscar Aluno", command=nova_janela_buscar_aluno)
    botao_buscar_aluno.grid(column=0, row=3, padx=50, pady=20)
    botao_fechar_cadastro = Button(nova_janela_cadastrar_aluno, text="Fechar",
                                   command=nova_janela_cadastrar_aluno.destroy)
    botao_fechar_cadastro.grid(column=0, row=4, padx=50)
    nova_janela_cadastrar_aluno.mainloop()


def nova_janela_inserir_aluno():
    nova_janela_inserir_aluno = Tk()
    nova_janela_inserir_aluno.title("Cadastrar Aluno")
    nova_janela_inserir_aluno.geometry("250x250")
    nova_janela_inserir_aluno.resizable(False, False)
    nova_janela_inserir_aluno.focus_force()

    Label(nova_janela_inserir_aluno, text="Nome").place(x=10, y=10)
    nome = Entry(nova_janela_inserir_aluno)
    nome.place(x=10, y=30, width=200, height=20)

    Label(nova_janela_inserir_aluno, text="Matricula").place(x=10, y=60)
    matricula = Entry(nova_janela_inserir_aluno)
    matricula.place(x=10, y=80, width=100, height=20)

    Label(nova_janela_inserir_aluno, text="Email").place(x=10, y=110)
    email = Entry(nova_janela_inserir_aluno)
    email.place(x=10, y=130, width=150, height=20)

    Label(nova_janela_inserir_aluno, text="Telefone").place(x=10, y=160)
    telefone = Entry(nova_janela_inserir_aluno)
    telefone.place(x=10, y=180, width=90, height=20)

    Button(nova_janela_inserir_aluno, text="SALVAR").place(x=10, y=210, width=100, height=20)
    Button(nova_janela_inserir_aluno, text="VOLTAR", command=nova_janela_inserir_aluno.destroy).place(x=140, y=210,
                                                                                                      width=100,
                                                                                                      height=20)


def nova_janela_excluir_aluno():
    nova_janela_excluir_aluno = Toplevel()
    nova_janela_excluir_aluno.title("Cadastrar Aluno")
    nova_janela_excluir_aluno.geometry("250x250")
    nova_janela_excluir_aluno.resizable(False, False)
    nova_janela_excluir_aluno.focus_force()

    # Mostrar os nomes dos alunos

    Button(nova_janela_excluir_aluno, text="EXCLUIR ALUNO").place(x=10, y=210, width=100, height=20)
    Button(nova_janela_excluir_aluno, text="VOLTAR", command=nova_janela_excluir_aluno.destroy).place(x=140, y=210,
                                                                                                      width=100,
                                                                                                      height=20)


def nova_janela_buscar_aluno():
    nova_janela_buscar_aluno = Toplevel()
    nova_janela_buscar_aluno.title("Buscar Aluno")
    nova_janela_buscar_aluno.geometry("250x250")
    nova_janela_buscar_aluno.resizable(False, False)
    nova_janela_buscar_aluno.focus_force()

    frame_direita = Frame(nova_janela_buscar_aluno, width=588, height=403, relief='flat')
    frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

    lista = [[1, 'Joao 1', '2019111', 'joao@mail.com', 123456789],
             [2, 'Joao 2', '2019222', 'joao@mail.com', 123456789],
             [3, 'Joao 3', '2019333', 'joao@mail.com', 123456789],
             [4, 'Joao 4', '2019444', 'joao@mail.com', 123456789],
             [5, 'Joao 5', '2019555', 'joao@mail.com', 123456789],
             ]

    # criando cabeçalho e tabela
    tabela_head = ['ID', 'Nome', 'Matricula', 'Email', 'Telefone']
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # barra de rolagem vertical
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # barra de rolagem horizontal
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "center", "center"]
    h = [30, 170, 140, 100, 120, 50, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in lista:
        tree.insert('', 'end', values=item)

    Button(nova_janela_buscar_aluno, text="SELECIONAR").place(x=10, y=210, width=100, height=20)
    Button(nova_janela_buscar_aluno, text="VOLTAR", command=nova_janela_buscar_aluno.destroy).place(x=140, y=210,
                                                                                                    width=100,
                                                                                                    height=20)

# INFORMAR PRESENÇA
def nova_janela_informar_presenca():
    nova_janela_informar_presenca = Toplevel()
    nova_janela_informar_presenca.title("Informar Presença")
    nova_janela_informar_presenca.geometry("190x200")
    nova_janela_informar_presenca.resizable(False, False)

    botao_informar_presenca = Button(nova_janela_informar_presenca, text="Informar Presença")
    botao_informar_presenca.grid(column=0, row=1, padx=40, pady=20)
    botao_tolalizar_falta = Button(nova_janela_informar_presenca, text="Totalizar Falta")
    botao_tolalizar_falta.grid(column=0, row=2, padx=40)
    botao_fechar = Button(nova_janela_informar_presenca, text="Fechar", command=nova_janela_informar_presenca.destroy)
    botao_fechar.grid(column=0, row=4, padx=40, pady=20)
    nova_janela_informar_presenca.mainloop()


# INFORMAR AVALIAÇÃO
def nova_janel_informar_avaliacao():
    nova_janela_informar_avaliacao = Toplevel()
    nova_janela_informar_avaliacao.title("Informar Avaliaçao")
    nova_janela_informar_avaliacao.geometry("190x200")
    nova_janela_informar_avaliacao.resizable(False, False)

    botao_primeira_avaliacao = Button(nova_janela_informar_avaliacao, text="1° Avaliação")
    botao_primeira_avaliacao.grid(column=0, row=1, padx=40, pady=20)
    botao_segunda_avaliacao = Button(nova_janela_informar_avaliacao, text="2° Avaliação")
    botao_segunda_avaliacao.grid(column=0, row=2, padx=40)
    botao_outras_avaliacoes = Button(nova_janela_informar_avaliacao, text="Outras Avaliações")
    botao_outras_avaliacoes.grid(column=0, row=3, padx=40, pady=20)
    botao_fechar = Button(nova_janela_informar_avaliacao, text="Fechar", command=janela)
    botao_fechar.grid(column=0, row=4, padx=40)
    nova_janela_informar_avaliacao.mainloop()


# MENU INICIAL
def janela():
    janela = Tk()
    janela.title("nome do programa")
    janela.geometry("190x200")
    janela.resizable(False, False)

    botao_cadastraraluno = Button(janela, text="Cadastrar Aluno", command=nova_janela_cadastrar_aluno)

    botao_cadastraraluno.grid(column=0, row=1, padx=40, pady=20)
    botao_informapresenca = Button(janela, text="Informa Presença", command=nova_janela_informar_presenca)
    botao_informapresenca.grid(column=0, row=2, padx=40)
    botao_informaavaliacao = Button(janela, text="Informa Avaliação", command=nova_janel_informar_avaliacao)
    botao_informaavaliacao.grid(column=0, row=3, padx=40, pady=20)
    botao_sair = Button(janela, text="Sair", command=exit)
    botao_sair.grid(column=0, row=4, padx=40)
    janela.mainloop()


janela()
