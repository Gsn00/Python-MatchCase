num = float(input('Digite um número: '))
calculo = int(input('1 - O dobro\n2 - A metade\n3 - 10% do número\nEscolha uma das operações acima: '))

match calculo:
    case 1:
        print(num * 2)
    case 2:
        print(num / 2)
    case 3:
        print(num * .1)
    case _:
        print('Nenhuma das opções foram selecionadas')