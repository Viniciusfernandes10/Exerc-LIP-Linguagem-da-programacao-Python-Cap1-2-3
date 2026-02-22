def dict_contato(nome, telefone, endereco):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "endereco": endereco
    }
    return contato


nome = input()
telefone = input()
endereco = input()

contato = dict_contato(nome, telefone, endereco)

print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Endereço: {contato['endereco']}.")