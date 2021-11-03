
def teste_arquivo():
    if not arquivoExiste(arq):
        criarArquivo(arq)


def arquivoExiste(nome):

    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def ler_saldo(msg):
    dado_ok = False
    while not dado_ok:
        try:
            saldo = float(input(msg))
            if (saldo > 0):
                dado_ok = True
            else:
                print('Saldo inicial não pode ser 0 ou menor')
        except ValueError:
            print('\033[31mERRO: Digite um número. \033[m')
    return saldo


def ler_numero_conta(msg):
    dado_ok = False
    while not dado_ok:
        try:
            num = int(input(msg))
            if (num > 0):
                dado_ok = True
            else:
                print(
                    'O número da conta tem que ser maior do que 0.')
        except ValueError:
            print('\033[31mERRO: Digite um número. \033[m')
    return num


def val_nome():
    dado_ok = False
    while not dado_ok:
        try:
            nome = str(input('Entre com seu nome: '))
            dado_ok = True
        except ValueError:
            print('\033[31mERRO: Digite uma letra. \033[m')
    return nome


def ler_nome():
    while True:
        nome = val_nome()
        if (len(nome.split(' ')) >= 2):
            break
        print('O nome precisa de espaços')
    return nome


def linha(tam=50):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(50))  # centralizar 52 caracteres
    print(linha())


def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m -  {item}')
        c += 1
    print(linha())
    opc = validar_escolha('Digite sua opção: ')
    return opc


def validar_escolha(msg):
    dado_ok = False
    while not dado_ok:
        try:
            num = int(input(msg))
            dado_ok = True
        except ValueError:
            print('\033[31mERRO: Digite um número. \033[m')
    return num


def ler_contas(lista):
    with open('contas.txt', 'rt') as arq:
        conta = arq.readline()
        while (conta != ''):
            conta = conta.strip('\n')
            conta = conta.split(';')
            conta[0], conta[2] = int(
                conta[0]), float(conta[2])
            lista.append(conta)
            conta = arq.readline()
        print(lista)
    return lista


def mostrar_contas(nome):
    for conta in lista:
        print(conta)


def verificar(lista, contas):
    achou = False
    for conta in lista:
        if conta[0] == contas:
            achou = True
    return achou


def gravar_conta(lista, conta):
    with open('contas.txt', 'wt') as arq:
        for conta in lista:
            arq.write(f'{conta[0]};{conta[1]};{conta[2]} \n')
    print('Conta gravada')


def incluir_conta(lista):
    conta = []
    cabeçalho('Incluir Conta')
    contas = ler_numero_conta('Conta: ')
    if verificar(lista, contas) == False:
        nome = ler_nome()
        saldo = ler_saldo('Digite seu saldo: ')
        if (saldo > 0):
            conta.append(contas)
            conta.append(nome)
            conta.append(saldo)
            lista.append(conta)
            print(lista)
            print(conta)
        else:
            print('Saldo deve ser maior ou igual a 0')
    else:
        print('Conta já existe')


def excluir_conta(lista):
    print(lista)
    cabeçalho('Excluir Conta')
    contas = ler_numero_conta('Conta: ')
    for conta in lista:
        if (conta[0] == contas):
            if conta[2] != 0:
                print(conta)
                print('Saldo deve ser nulo para exclusão')
            else:
                print(conta)
                lista.remove(conta)
                print('Conta excluída')


def alterar_conta(lista):
    while True:
        print('1. Sacar' '\n' '2. Depositar' '\n' '3. Sair' '\n')
        resp = validar_escolha('Deseja sacar ou depositar?\n')
        if resp == 1:
            sacar(lista)
        elif resp == 2:
            depositar(lista)
        elif resp == 3:
            print('Saindo')
            break
        else:
            print('Digite um número válido')


def depositar(lista):
    print(lista)
    contas = ler_numero_conta('Conta: ')
    for conta in lista:
        if (conta[0] == contas):
            saldo = ler_saldo('Digite o valor do depósito: ')
            if (saldo > 0):
                saldonovo = (conta[2] + saldo)
                if (saldonovo < 0):
                    print('Quantia inexistente')
                else:
                    conta[2] = saldonovo
                print('\n''Seu novo saldo é de:', saldonovo)
            else:
                print('Digite um valor maior do que 0')


def sacar(lista):
    print(lista)
    contas = ler_numero_conta('Conta: ')
    for conta in lista:
        if (conta[0] == contas):
            saldo = ler_saldo('Digite o valor do saque: ')
            if (saldo > 0):
                saldonovo = (conta[2] - saldo)
                if (saldonovo < 0):
                    print('Quantia inexistente')
                else:
                    conta[2] = saldonovo
                    print('\n''Seu novo saldo é de:', saldonovo)
            else:
                print('Digite um valor maior do que 0')


def relatorio(lista):
    while True:
        print('1. Clientes com saldo negativo' '\n' '2. Clientes com saldo positivo' '\n' '3. Listar todas as contas' '\n' '4. Sair' '\n')
        resp = validar_escolha('Digite sua opção: ')
        if resp == 1:
            saldo_negativo(lista)
        elif resp == 2:
            saldo_positivo(lista)
        elif resp == 3:
            mostrar_contas(arq)
        elif resp == 4:
            print('Saindo...')
            break
        else:
            print('Digite um número válido')


def saldo_negativo(lista):
    for conta in lista:
        if conta[2] < 0:
            print(conta)


def saldo_positivo(lista):
    saldo = ler_saldo('Mostrar contas acima do valor: ')
    for conta in lista:
        if conta[2] > saldo:
            print(conta)


arq = 'contas.txt'
lista = []
conta = []
ler_contas(lista)

while True:
    reply = menu(['Inclusão de conta', 'Alteração de saldo',
                  'Exclusão de conta', 'Relatórios gerenciais', 'Sair'])
    if (reply == 1):
        incluir_conta(lista)
    elif (reply == 2):
        alterar_conta(lista)
    elif (reply == 3):
        excluir_conta(lista)
    elif (reply == 4):
        relatorio(lista)
    elif (reply == 5):
        cabeçalho('Saindo...')
        break
    else:
        print('\033[31mERRO: Digite uma opção válida.\033[m')
gravar_conta(lista, conta)

# gravar contas no final do while
# split nome
# trocar o mostrar contas
