n = input("Digite um número inteiro: ")

soma = 0

for i in range(0, len(n)):
    soma += int(n[i])

print(soma)