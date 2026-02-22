def verificar_conjuntos():
  conjunto_a = set()
  conjunto_b = set()

  for i in range(3):
    num = int(input())
    conjunto_a.add(num)

  for i in range(3):
    num = int(input())
    conjunto_b.add(num)

  uniao = conjunto_a | conjunto_b
  intersecao = conjunto_a & conjunto_b
  diferenca = conjunto_a - conjunto_b
  
  return uniao, intersecao, diferenca

uniao, intersecao, diferenca = verificar_conjuntos()
print(f"União: {uniao}")
print(f"Interseção: {intersecao}")
print(f"Diferença: {diferenca}")