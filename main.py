maior = int(-99999999)
posicao = int(0)
for x in range(1, 101):
    numero = int(input())
    if (numero > maior):
        maior = numero
        posicao = x
print(maior)
print(posicao)