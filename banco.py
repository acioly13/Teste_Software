# importanto SQLite
import sqlite3 as lite

# criando conexão
con = lite.connect('dados.db')

# criando tabelas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE aluno(id INTEGER PRIMARY KEY, nome TEXT, local TEXT, email TEXT, ddd_num INTEGER )")