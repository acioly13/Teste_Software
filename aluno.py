# Funcionalidades e Views Alunos

# importanto SQLite
import sqlite3 as lite

# criando conexão
con = lite.connect('dados.db')


# Inserir Aluno
lista = ['teste', 201929999, 'teste@email.com', 666]
with con:
    cur = con.cursor()
    query = "INSERT INTO aluno(nome, matricula, email, telefone) VALUES(?, ?, ?, ?)"
    cur.execute(query, lista)

# Atualizar Aluno
lista = ['teste2', 2]
with con:
    cur = con.cursor()
    query = "UPDATE aluno SET nome=? WHERE id=?"
    cur.execute(query, lista)

# Listar Aluno
with con:
    cur = con.cursor()
    query = "SELECT * FROM aluno"
    cur.execute(query)
    info = cur.fetchall()
    print(info)

# Deletar Aluno
lista = [2]
with con:
    cur = con.cursor()
    query = "DELETE FROM aluno WHERE id=?"
    cur.execute(query, lista)
