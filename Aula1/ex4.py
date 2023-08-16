renda = int(input('Informe sua renda: '))
if renda < 1903.99:
    print('Aliquota: 0\n Imposto: 0\n')
elif renda >= 1903.99 and renda <= 2826.65:
    print('Aliquota: 7,5%\n Imposto:'renda * (7.5/100))
elif renda >= 2826.66 and renda <= 3751.05:
    print('Aliquota: ')