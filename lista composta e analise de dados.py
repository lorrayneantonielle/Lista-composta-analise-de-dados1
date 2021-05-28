temp = []
princ = []
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp in 'N':
        break
print(f'Os dados foram {princ}')
print(f'Ao todo foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}Kg.')
for p in princ:
    if p[1] == maior:
        print(p[0])
print(f'O menor peso foi de {menor}Kg.')
for p in princ:
   if p[1] == menor:
       print(p[0])


