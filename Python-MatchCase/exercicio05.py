print('1 - Picanha R$25,00')
print('2 - Lasanha R$20,00')
print('3 - Strogonoff R$20,00')
print('4 - Bife Acebolado R$15,00')
print('5 - Pão com Ovo R$5,00')
prato = int(input('Selecione um dos pratos acima: '))
print('Você aceita pagar uma taxa de 10%?')
print('1 - Aceito')
print('2 - Não aceito')
aceitouTaxa = int(input('Digite sua resposta: '))

match aceitouTaxa:
    case 1:
        match prato:
            case 1:
                print(f'Valor com taxa R${(25 * 1.1):.2f}')
            case 2:
                print(f'Valor com taxa R${(20 * 1.1):.2f}')
            case 3:
                print(f'Valor com taxa R${(20 * 1.1):.2f}')
            case 4:
                print(f'Valor com taxa R${(15 * 1.1):.2f}')
            case 5:
                print(f'Valor com taxa R${(5 * 1.1):.2f}')
    case 2:
        match prato:
            case 1:
                print(f'Valor com taxa R$25.00')
            case 2:
                print(f'Valor com taxa R$20.00')
            case 3:
                print(f'Valor com taxa R$20.00')
            case 4:
                print(f'Valor com taxa R$15.00')
            case 5:
                print(f'Valor com taxa R$5.00')
