a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4 * a * c
r1 = (-b + delta**(1/2))/(2*a)
r2 = (-b - delta**(1/2))/(2*a)

print("delta: ", delta)
print("resultado 1: ", r1)
print('resultado 2: ', r2)
