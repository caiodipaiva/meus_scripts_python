import sqlite3
# sqlite3 é uma biblioteca do Python para trabalhar com bancos SQLite.

conexao = sqlite3.connect("locadora.db")
# Criamos uma conexão. Se o arquivo locadora.db não existir, o SQLite cria.

cursor = conexao.cursor()
# Criamos um cursor para EXECUTAR os comandos SQL.


# =========================
# CRIAÇÃO DA TABELA FILMES
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    preco REAL
)
""")

conexao.commit()
# O commit() confirma a alteração.


# =========================
# INSERIR FILMES NO BANCO
# =========================

cursor.execute("""
INSERT INTO filmes (titulo, preco)
SELECT 'matrix', 13
WHERE NOT EXISTS (
    SELECT 1 FROM filmes WHERE titulo = 'matrix'
)
""")

cursor.execute("""
INSERT INTO filmes (titulo, preco)
SELECT 'clube da luta', 10
WHERE NOT EXISTS (
    SELECT 1 FROM filmes WHERE titulo = 'clube da luta'
)
""")

conexao.commit()


# =========================
# VER FILMES DO BANCO
# =========================

def listar_filmes():

    try:
        cursor.execute("SELECT titulo, preco FROM filmes")
        filmes = cursor.fetchall()

        for filme, preco in filmes:
            print(f"Filme: {filme} | Preço: R$ {preco:.2f}")

    except sqlite3.Error as erro:
        print(f"Erro ao consultar os filmes: {erro}")


# =========================
# TABELA DE ALUGUÉIS
# =========================

try:

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alugueis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente TEXT,
        filme TEXT,
        preco REAL
    )
    """)

    conexao.commit()

except sqlite3.Error as erro:
    print(f"Erro ao criar tabela de aluguéis: {erro}")


# =========================
# OPÇÃO 2 - ALUGAR FILME
# =========================

def alugar_filme():

    try:

        print("\n=== FILMES DISPONÍVEIS ===")

        cursor.execute("SELECT titulo, preco FROM filmes")
        filmes = cursor.fetchall()

        for filme, preco in filmes:
            print(f"Filme: {filme} | Preço: R$ {preco:.2f}")

        filme_escolhido = input("\nQual filme você deseja?: ").strip()

        cursor.execute(
            "SELECT titulo, preco FROM filmes WHERE titulo = ?",
            (filme_escolhido,)
        )

        filme_encontrado = cursor.fetchone()

        if filme_encontrado:

            titulo, preco = filme_encontrado

            print(f"\nFilme escolhido: {titulo}")
            print(f"Preço: R$ {preco:.2f}")

            pagamento = input(
                "Deseja prosseguir com o pagamento? (s/n): "
            ).lower().strip()

            if pagamento == "s":

                nome_cliente = input("Digite seu nome: ").strip()

                if not nome_cliente:
                    print("O nome do cliente não pode ficar vazio.")
                    return

                cursor.execute("""
                INSERT INTO alugueis (cliente, filme, preco)
                VALUES (?, ?, ?)
                """, (nome_cliente, titulo, preco))

                conexao.commit()

                print(f"Pagamento realizado com sucesso! Obrigado {nome_cliente}!")

            elif pagamento == "n":

                print("Pagamento cancelado.")

            else:

                print("Opção de pagamento inválida.")

        else:

            print("Infelizmente não temos esse filme.")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


# =========================
# OPÇÃO 3 - CADASTRAR FILME
# =========================

def cadastrar_filme():

    novo_filme = input("Digite o filme: ").strip()

    if not novo_filme:
        print("O nome do filme não pode ficar vazio.")
        return

    try:

        preco = float(input("Digite o preço: "))

        if preco <= 0:
            print("O preço deve ser maior que zero.")
            return

        cursor.execute("""
        INSERT INTO filmes (titulo, preco)
        VALUES (?, ?)
        """, (novo_filme, preco))

        conexao.commit()

        print("Filme adicionado com sucesso!")

    except ValueError:
        print("Digite um preço válido. Exemplo: 13.90")

    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar filme: {erro}")


# =========================
# OPÇÃO 4 - APAGAR FILME
# =========================

def apagar_filme():

    delete_filme = input("Digite um filme que deseja apagar: ").strip()

    if not delete_filme:
        print("O nome do filme não pode ficar vazio.")
        return

    try:

        cursor.execute("""
        DELETE FROM filmes
        WHERE titulo = ?
        """, (delete_filme,))

        conexao.commit()

        if cursor.rowcount > 0:
            print("Filme apagado com sucesso!")
        else:
            print("Filme não encontrado.")

    except sqlite3.Error as erro:
        print(f"Erro ao apagar filme: {erro}")


# =========================
# PROGRAMA PRINCIPAL
# =========================

while True:

    print("\n=== BEM-VINDO À LOCADORA! ===")
    print("[1] Filmes disponíveis")
    print("[2] Alugar um Filme")
    print("[3] Cadastrar filme")
    print("[4] Apagar Filme")
    print("[5] Sair")

    try:

        escolha = int(input("Escolha: "))

    except ValueError:

        print("Digite apenas o número da opção.")
        continue


    if escolha == 1:

        listar_filmes()


    elif escolha == 2:

        alugar_filme()


    elif escolha == 3:

        cadastrar_filme()


    elif escolha == 4:

        apagar_filme()


    elif escolha == 5:

        print("Ok, até mais!")
        break


    else:

        print("Opção inválida. Escolha uma opção de 1 a 5.")


# Fecha a conexão com o banco quando o programa termina.
conexao.close()

