# Construção do dicionário
tabela = {
  'alface': 0.45,
  'batata': 1.20,
  'tomate': 2.30,
  'feijão': 1.5
}

# verificando o preço da batata e do feijão
print(tabela["batata"])
print(tabela["feijão"])

# alterando o preço do tomate
tabela["tomate"] = 1.80
print(tabela["tomate"])

# inserindo um novo produto "arroz" e atribuindo o preço dele
tabela["arroz"] = 3.00
print(tabela)

# verificando se o arroz está na tabela
if "arroz" in tabela:
  print("Tem arroz na tabela.")
else:
  print("Não tem arroz na tabela.")

# printando as chaves
for chave in tabela.keys():
  print(chave)

# printando os valores
for valor in tabela.values():
  print(valor)

# acessando e printando as chaves e os valores
for chave, valor in tabela.items():
  print(f"{chave} = {valor}")

# removendo o arroz da tabela
del tabela["arroz"]
print(tabela)