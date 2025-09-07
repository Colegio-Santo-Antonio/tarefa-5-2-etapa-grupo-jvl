# Leia uma linha com o número do cartão

# Júlia Diniz, Letícia Cozzi, Vitória Vieira
numero = input()
impares = []
for i in numero[-1::-2]:
  impares.append(int(i))
pares = []
for i in numero[-2::-2]:
  dobro = 2*int(i)
  if dobro > 9:
    dobro = dobro - 9
  pares.append(dobro)
soma = sum(pares) + sum(impares)
if int(soma/10) == soma/10:
  print("Cartão válido")
else:
  print("Cartão inválido")


# TODO: implemente a verificação pelo algoritmo de Luhn
# Siga as dicas do README.

# Ao final, imprima exatamente:
# print("Cartão válido")  ou  print("Cartão inválido")
