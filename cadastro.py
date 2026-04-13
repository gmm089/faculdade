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
                print("ID NOME MATRICULA NOTA 1 NOTA 2 NOTA 3 NOTA 4 MEDIA SITUACAO")

                for aluno in alunos:
                    print(aluno)
            case 3:
                busca = input("Digite o nome ou a matricula do aluno procurado:")
                c.execute('''
                  SELECT *
                        FROM alunos
                        WHERE matricula = ?
                        OR nome LIKE ?
                        ''', (busca, f'%{busca}%'))

                aluno = c.fetchall()
                if aluno:
                    print("ID NOME MATRICULA NOTA 1 NOTA 2 NOTA 3 NOTA 4 MEDIA SITUACAO")
                    print(aluno)
                else:
                    print("\nAluno não encontrado")
            case 4:
                matricula = input("\nDigite a matrícula do aluno:  ").strip().upper()
                c.execute("SELECT * FROM alunos WHERE matricula = ?", (matricula,))
                aluno = c.fetchone()
                if aluno:
                    print("  Aluno encontrado!    ")
                    print(aluno)
                    opc = int(input("1 - Editar nome\n2 - Editar Nota 1\n3 - Editar Nota 2\n4 - Editar Nota 3\n5 - Editar Nota 4\nOPCAO:"))
                    if opc == 1:
                        editnome = input("Informe o novo nome: ")
                        c.execute('''
                            UPDATE alunos SET nome = ? WHERE matricula = ?
                        ''',(editnome,matricula))
                        conn.commit()
                    elif opc == 2:
                        editnota1 = float(input("Informe o nova nota: "))
                        media = (editnota1 + aluno[4] + aluno[5] + aluno[6]) / 4
                        if media > 6.9:
                            situacao = "APROVADO"
                        else:
                            situacao = "REPROVADO"
                        c.execute('''
                                  UPDATE alunos
                                  SET nota1 = ?, media = ?, situacao = ?
                                  WHERE matricula = ?
                                  ''', (editnota1,media,situacao,matricula))
                        conn.commit()
                    elif opc == 3:
                        editnota2 = float(input("Informe o nova nota: "))
                        media = (editnota2 + aluno[3] + aluno[5] + aluno[6]) / 4
                        if media > 6.9:
                            situacao = "APROVADO"
                        else:
                            situacao = "REPROVADO"
                        c.execute('''
                                  UPDATE alunos
                                  SET nota2    = ?,
                                      media    = ?,
                                      situacao = ?
                                  WHERE matricula = ?
                                  ''', (editnota2, media, situacao, matricula))
                        conn.commit()
                    elif opc == 4:
                        editnota3 = float(input("Informe o nova nota: "))
                        media = (editnota3 + aluno[4] + aluno[3] + aluno[6]) / 4
                        if media > 6.9:
                            situacao = "APROVADO"
                        else:
                            situacao = "REPROVADO"
                        c.execute('''
                                  UPDATE alunos
                                  SET nota3    = ?,
                                      media    = ?,
                                      situacao = ?
                                  WHERE matricula = ?
                                  ''', (editnota3, media, situacao, matricula))
                        conn.commit()
                    elif opc == 5:
                        editnota4 = float(input("Informe o nova nota: "))
                        media = (editnota4 + aluno[4] + aluno[5] + aluno[3]) / 4
                        if media > 6.9:
                            situacao = "APROVADO"
                        else:
                            situacao = "REPROVADO"
                        c.execute('''
                                  UPDATE alunos
                                  SET nota4    = ?,
                                      media    = ?,
                                      situacao = ?
                                  WHERE matricula = ?
                                  ''', (editnota4, media, situacao, matricula))
                        conn.commit()
                else:
                    print("Aluno nao encontrado")
            case 5:
                matricula = input("Digite o matricula do aluno: ")
                c.execute('''SELECT * FROM alunos WHERE matricula = ?''', (matricula,))
                aluno = c.fetchone()
                if not aluno:
                    print("Nenhum aluno foi encontrado")
                else:
                    print(aluno)
                    confirmacao = input("Deseja deletar esse aluno? S/N:")
                    if confirmacao == "S":
                        c.execute("DELETE FROM alunos WHERE matricula = ?", (matricula,))
                        conn.commit()
                        print("Aluno deletado com sucesso")
                    else:
                        print("Opcao cancelada")
            case  6:
                break
            case _:
                print("OPCAO INVALIDA")



