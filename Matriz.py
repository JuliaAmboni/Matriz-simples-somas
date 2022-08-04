matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
lista1 = []
lista2 = []
soma = soma2 = somacol = maior = 0

for i in range(0, 3):
    for c in range (0, 3):
        matriz[i][c] = int(input(f'Digite um valor para posição [{i}, {c}]: '))
        if matriz[i][c] % 2 == 0:
            lista1.append(matriz[i][c])
            soma = sum(lista1)
        else:
            lista2.append(matriz[i][c])
            soma2 = sum(lista2)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[i][c]:^5}]', end = '')
    print()
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores impares é {soma2}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
for i in range(0, 3):
    somacol += matriz[i][2]
print(f'A soma da tarceira coluna é {somacol}')
