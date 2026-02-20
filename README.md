# Exercícios de Lógica em Python 🐍

Este repositório contém exercícios de lógica de programação resolvidos em Python,
organizados por capítulos.

📘 **Livro base:**  
**Python Básico - Um Guia para Iniciantes e Universitários**  
✍️ Autor: Helton Maia

🔗 Livro virtual:  
https://heltonmaia.com/pythonbook/intro.html

## [Capítulo 1: Introdução à programação em Python](https://heltonmaia.com/pythonbook/chapters/ch1/ch1.html)

### **Lista de exercícios**

## – Exercício 01 –

Arquivo: `capitulo1/ex01.py`

### Enunciado

Escreva um programa que imprima a famosa mensagem do mundo da programação.

Neste exercício, você deve simplesmente exibir uma mensagem na tela.
Não é necessário ler nenhuma entrada do usuário, apenas utilizar o comando `print`.

### Exemplo de saída esperada

**Saída:**
Hello World!

### Resolução

```python
print("Hello World!!")
```

---

## – Exercício 02 –

Arquivo: `capitulo1/ex02.py`

### Enunciado

Neste exercício, você deve ler duas entradas: o nome de um aluno e sua matrícula. Em seguida, exiba uma mensagem de boas-vindas formatada com esses dados.

### Exemplo de saída esperada

**Entrada:**

Python da Silva

2024123456

**Saída:**

Olá Python da Silva Matrícula: 2024123456 Seja bem vindo!

### Resolução

```python
def informacao():
    nome = input("Digite seu nome: ")
    matricula = input("Digite sua matrícula: ")
    return nome, matricula

nome, matricula = informacao()
print(f"Olá {nome} Matrícula: {matricula} Seja bem-vindo!")
```

---

## – Exercício 03 –

Arquivo: `capitulo1/ex03.py`

### Enunciado

Informações de um Pedido. Crie um programa que deve ler quatro entradas do usuário:

- Nome do cliente
- Produto comprado
- Quantidade adquirida
- Valor unitário do produto

Em seguida, exiba uma mensagem formatada informando os detalhes da compra, incluindo o valor total.

### Exemplo de saída esperada

**Entrada:**

Ana Souza  
Livro de Python  
1
45.50

Saída:

Pedido confirmado: Livro de Python
Valor total: R$ 45.50
Obrigado pela preferência!

### Resolução

```python
def pedido():
  nome = input("Digite seu nome: ")
  produto = input("Digite o produto solicitado: ")
  quantidade = int(input("Digite a quantidade: "))
  valor = float(input("Digite o valor do produto: "))
  return nome, produto, quantidade, valor

nome, produto, quantidade, valor = pedido()
print(f"Pedido confirmado: {produto} \nValor total: R${valor * quantidade:.2f} \nObrigado pela preferência {nome}!")

```

---

## [Capítulo 2: Tipos de dados e Estruturas Condicionais](https://heltonmaia.com/pythonbook/chapters/ch2/ch2.html)

### **Lista de exercícios**

## – Exercício 01 –

Arquivo: `capitulo2/ex01.py`

### Enunciado

Escreva um programa que solicita ao usuário dois valores, um do tipo inteiro (`int`) e outro do tipo ponto flutuante (`float`). Após receber esses valores como entrada, o programa deve atribuí-los a duas variáveis distintas e, em seguida, imprimir na tela o resultado das seguintes operações matemáticas:

- Soma dos dois valores.
- Subtração do valor do tipo float pelo valor do tipo inteiro.
- Multiplicação dos dois valores.
- Divisão do valor do tipo inteiro pelo valor do tipo float.

Certifique-se de formatar adequadamente a saída dos resultados.

### Exemplo de saída esperada

**Entrada:**

Ana Souza  
Livro de Python  
1
45.50

**Saída:**

Pedido confirmado: Livro de Python
Valor total: R$ 45.50
Obrigado pela preferência!

### Resolução

```python
def dois_valores():
  a = int(input("Digite um número inteiro: "))
  b = float(input("Digite um número quebrado:  "))
  return a, b

a, b = dois_valores()
print(f"Soma: {a + b} \nSubtração: {b - a} \nMultiplicação: {a * b} \nDivisão: {a / b}")

```

---

## – Exercício 02 –

Arquivo: `capitulo2/ex02.py`

### Enunciado

Escreva um programa que solicite ao usuário que insira uma palavra ou frase. Em seguida, o programa deve imprimir o comprimento da string, a primeira letra da string, a última letra da string e a string invertida.

### Exemplo de saída esperada

**Teste 1**

Entrada:
True
true

Saída:
São iguais

**Teste 2**

Entrada:
True
False

Saída:
São diferentes

### Resolução

```python
def palavra_ou_frase():
  frase = input("Digite uma frase: ")
  quant_caracteres = len(frase)
  primeira_letra = frase[0]
  ultima_letra = frase[-1]
  string_invertida = frase[::-1]
  return frase, quant_caracteres, primeira_letra, ultima_letra, string_invertida

frase, quant_caracteres, primeira_letra, ultima_letra, string_invertida = palavra_ou_frase()
print(f"{quant_caracteres} \n{primeira_letra} \n{ultima_letra} \n{string_invertida}")

```

---

## – Exercício 03 –

Arquivo: `capitulo2/ex03.py`

### Enunciado

Escreva um programa que compare duas strings fornecidas pelo usuário, considerando valores booleanos "True" ou "False". O programa deve ignorar diferenças de capitalização (maiúsculas e minúsculas) e imprimir na tela se as strings são iguais ou diferentes.

### Exemplo de saída esperada

**Teste 1**

Entrada:
True
true

Saída:
São iguais

**Teste 2**

Entrada:
True
False

Saída:
São diferentes

### Resolução

```python
def comparar():
  string1 = input("Escreva True ou False: ").lower()
  string2 = input("Escreva True ou False: ").lower()
  if string1 == string2:
    print("São iguais")
  else:
    print("São diferentes")
  return string1, string2

a, b = comparar()

```

---
