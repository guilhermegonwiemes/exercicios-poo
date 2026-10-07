nomes = []
notas1 = []
notas2 = []

def cadastrar():
    nome = input('Nome do estudante: ')
    nota1 = float(input('1ª nota: ')) #ao usar float() aqui e na linha abaixo, fazemos o CASTING, convertendo o tipo
    nota2 = float(input('2ª nota: '))

    nomes.append(nome)
    notas1.append(nota1)
    notas2.append(nota2)

def calcular_media(indice):
    media = (notas1[indice] + notas2[indice]) / 2
    return media

def situacao(indice):
    media = calcular_media(indice)
    if media >= 6:
        return 'Aprovado'
    elif media >= 4:
        return 'Recuperação'
    else:
        return 'Reprovado'

def listar():
    if len(nomes) == 0:
        print('Nenhum estudante cadastrado.')
        return
    print(f'\n{"NOME":<16}{"N1":<7}{"N2":<7}{"MÉDIA":<8}{"SITUAÇÃO":<14}')
    for i in range(len(nomes)):
        print(f'{nomes[i]:<16}{notas1[i]:<7}{notas2[i]:<7}{calcular_media(i):<8.1f}{situacao(i):<14}')

def media_da_turma():
    if len(nomes) == 0:
        print('Nenhum estudante cadastrado.')
        return

    soma = 0
    for i in range (len(nomes)):
        soma = soma + calcular_media(i)
    print(f'\nMédia da turma: {soma / len(nomes):.1f}')

def menu():
    while True:
        print('\n1 - Cadastrar Estudante')
        print('2 - Listar Estudantes')
        print('3 - Média da Turma')
        print('4 - Sair')
        opcao = input('\nEscolha uma opção: ')

        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            media_da_turma()
        elif opcao == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida.')

menu()
