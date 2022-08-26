n = int(input("Digite um valor inteiro: "))


x = range(n-1, 1, -1)
fatorial = n

if (n > 1):
    for i in x:
        fatorial *= i
else:
    fatorial = 1


print(fatorial)