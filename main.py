import sqlite3


def criar_tabela():

    conn = sqlite3.connect("imc_usuarios.db")
    c = conn.cursor()


    c.execute('''
              CREATE TABLE IF NOT EXISTS imc_usuarios (
                  nome TEXT,
                  imc REAL
              )
              ''')
    conn.commit()
    conn.close()


def calcular_imc(nome, altura, peso):

    altura_metros = altura / 100
    imc = peso / (altura_metros ** 2)


    imc = round(imc, 2)


    conn = sqlite3.connect("imc_usuarios.db")
    c = conn.cursor()


    c.execute("INSERT INTO imc_usuarios VALUES (?, ?)", (nome, imc))
    conn.commit()
    conn.close()


    print(f"IMC calculado e armazenado com sucesso. Seu IMC é: {imc}")


def main():
    criar_tabela()

    while True:

        nome = input("Digite seu nome (ou 'sair' para encerrar): ")

        if nome.lower() == 'sair':
            break

        altura = float(input("Digite sua altura em centímetros: "))
        peso = float(input("Digite seu peso em quilogramas: "))


        calcular_imc(nome, altura, peso)


if __name__ == "__main__":
    main()