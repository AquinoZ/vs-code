qnt = int(input('digite quantos valores você tem: '))
n = 1
soma = 0
while n <= qnt:
  valor = int(input(f"Digite o {n}º número: "))
  soma += valor
  n += 1
print(f"Média: {soma / 5:5.2f}")