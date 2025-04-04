num = int(input('Digite um número inteiro: '))

match num % 3:
    case 0:
        print(f'O número {num} é múltiplo de 3')
    case _:
        print(f'O número {num} NÃO é múltiplo de 3')