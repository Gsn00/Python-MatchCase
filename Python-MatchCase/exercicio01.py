valor = float(input('Digite o valor da compra: '))
cliente = input('C = Comum\nF = Funcionário\nV = Vip\nDigite o tipo de cliente: ')

match cliente:
    case 'C' | 'c':
        print(f'O valor a ser cobrado para o cliente COMUM é {valor}')
    case 'F' | 'f':
        print(f'O valor a ser cobrado para o cliente FUNCIONÁRIO é {valor * .9}')
    case 'V' | 'v':
        print(f'O valor a ser cobrado para o cliente VIP é {valor * .95}')