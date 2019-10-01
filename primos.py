num = 1
contador = 1
num_max = int(input('Digite um numero :'))

while contador <= num_max:
    contador += 1
    num += 1
    if num %2 == 1:
        print(num)
    else:
        contador -= 1