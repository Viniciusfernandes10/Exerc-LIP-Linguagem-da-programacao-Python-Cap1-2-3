def informacao():
    nome = input("Digite seu nome: ")
    matricula = input("Digite sua matrícula: ")
    return nome, matricula

nome, matricula = informacao()
print(f"Olá {nome} Matrícula: {matricula} Seja bem-vindo!")
