# Funcionalidades e Views Alunos

# importanto SQLite
import sqlite3 as lite

# criando conexão
con = lite.connect('dados.db')


# Inserir Aluno
def inserir_aluno(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO aluno(nome, matricula, email, telefone) VALUES(?, ?, ?, ?)"
        cur.execute(query, i)


# Atualizar Aluno
def atualizar_aluno(i):
    with con:
        cur = con.cursor()
        query = "UPDATE aluno SET nome=? WHERE id=?"
        cur.execute(query, i)


# Deletar Aluno
def deletar_aluno(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM aluno WHERE id=?"
        cur.execute(query, i)


# Listar Aluno
def listar_aluno():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM aluno"
        cur.execute(query)
        info = cur.fetchall()
        for i in info:
            lista.append(i)
    return lista
