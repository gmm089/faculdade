import sqlite3


conn = sqlite3.connect('alunos.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    matricula TEXT NOT NULL,
    nota1 REAL NOT NULL,
    nota2 REAL NOT NULL,
    nota3 REAL NOT NULL,
    nota4 REAL NOT NULL,
    media REAL NOT NULL,
    situacao TEXT NOT NULL
    )
''')
conn.commit()

while True:

        print("1 - CADASTRAR UM ALUNO")
        print("2 - LISTAR ALUNOS")
        print("3 - BUSCAR ALUNO")
        print("4 - ALTERAR ALUNO")
        print("5 - DELETAR ALUNO")
        print("6 - SAIR")

        opcao = int(input("ESCOLHA UMA OPCAO: "))

        match opcao:
            case 1:
                nome = input("Nome do aluno: ")
                matricula = input("Matricula do aluno: ")
                nota1 = float(input("1 Nota do aluno: "))
                nota2 = float(input("2 Nota do aluno: "))
                nota3 = float(input("3 Nota do aluno: "))
                nota4 = float(input("4 Nota do aluno: "))
                media = (nota1 + nota2 + nota3 + nota4) / 4
                if(media > 6.9 ):
                    situacao = "APROVADO"
                else:
                    situacao = "REPROVADO"

                c.execute('''INSERT INTO alunos(nome, matricula, nota1, nota2, nota3, nota4, media, situacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''' , (nome, matricula, nota1, nota2, nota3, nota4, media, situacao))
                conn.commit()
            case 2:
                c.execute("SELECT * FROM alunos ORDER BY nome")
                alunos = c.fetchall()
                if not alunos:
                    print("Nenhum aluno foi cadastrado")
                print(f"{'ID'} {'NOME'} {'MATRICULA'} {'NOTA 1'} {'NOTA 2'} {'NOTA 3'} {'NOTA 4'} {'MEDIA'} {'SITUACAO'}")

                for aluno in alunos:
                    print(f" {aluno[0]} {aluno[1]} {aluno[2]} {aluno[3]} {aluno[4]} {aluno[5]} {aluno[6]} {aluno[7]} {aluno[8]}")
            case  6:
                break
            case _:
                print("OPCAO INVALIDA")



