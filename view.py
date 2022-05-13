# importanto SQLite
import sqlite3 as lite

# criando conexão
con = lite.connect('dados.db')


lista = ['teste', 201929999, 'teste@email.com', 666]
# Inserir Aluno
with con:
    cur = con.cursor()
    query = "INSERT INTO aluno(nome, matricula, email, telefone) VALUES(?, ?, ?, ?)"
    cur.execute(query, lista)
