numPalestra = int(input('1 - Linux\n2 - Banco de Dados\n3 - Windows Server\n4 - Lógica e Programação\n Escolha uma das palestras acima: '))

match numPalestra:
    case 1:
        print('A palestra de Linux será no auditório 1')
    case 2:
        print('A palestra de Banco de Dados será no auditório 2')
    case 3:
        print('A palestra de Windows Server será no auditório 3')
    case 4:
        print('A palestra de Lógica e Programação será no auditório principal')
    case _:
        print('Nenhuma palestra foi selecionada.')