import sqlite3

conexao = sqlite3.connect('dados.db')

# O cursor é quem executa os comandos SQL
cursor = conexao.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        email TEXT UNIQUE
    )
''')

# Definindo os dados, uma lista (ou tupla) contendo várias tuplas (cada tupla é uma linha)
novos_usuarios = [
    ('Mariana', 22, 'mari@email.com'),
    ('Carlos', 30, 'carlaograudo@emai.com'),
    ('Ana', 25, 'ana@email.com')
]

# executemany é usado para inserir vários registros de uma vez
cursor.executemany("INSERT OR IGNORE INTO usuarios (nome, idade, email) VALUES (?, ?, ?)", novos_usuarios)

conexao.commit()
print(f"{cursor.rowcount} registros inseridos com sucesso!")
print("Banco de dados e tabela criados com sucesso!")
