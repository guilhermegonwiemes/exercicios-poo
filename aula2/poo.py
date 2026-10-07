estudantes = []

def cadastrar_estudante():
    nome = input('Nome do estudante: ')
    while True:
        try:
            nota1 = float(input('1ª nota: '))
            break
        except ValueError:
            print('\n\33[31mErro: Por favor, insira valores numéricos válidos para as notas.\33[m')
            continue
    while True:
        try:
            nota2 = float(input('2ª nota: '))
            break
        except ValueError:
            print('\n\33[31mErro: Por favor, insira valores numéricos válidos para as notas.\33[m')
            continue
    Estudante(nome, nota1, nota2)

class Estudante:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        estudantes.append(self)

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        media = self.calcular_media()
        if media >= 6:
            return 'Aprovado'
        elif media >= 4:
            return 'Recuperação'
        else:
            return 'Reprovado'

    def listar():
        if len(estudantes) == 0:
            print('Nenhum estudante cadastrado.')
            return
        print(f'\n{'NOME':<16}{'N1':<7}{'N2':<7}{'MÉDIA':<8}{'SITUAÇÃO':<14}')
        for estudante in estudantes:
            print(f'{estudante.nome:<16}{estudante.nota1:<7}{estudante.nota2:<7}{estudante.calcular_media():<8.1f}{estudante.situacao():<14}')

    def media_turma():
        if len(estudantes) == 0:
            print('Nenhum estudante cadastrado.')
            return

        for estudante in estudantes:
            soma = sum(estudante.calcular_media() for estudante in estudantes)
            media = soma / len(estudantes)
        print(f'\nMédia da turma: {media:.1f}')

def menu():
    while True:
        print(f'\n{10 * "=-"} MENU {10 * "-="}\n')
        print('[1] - Cadastrar Estudante')
        print('[2] - Listar Estudantes')
        print('[3] - Média da Turma')
        print('[4] - Sair')
        opcao = input('\nEscolha uma opção: ')
        match opcao:
            case '1':
                cadastrar_estudante()
            case '2':
                Estudante.listar()
            case '3':
                Estudante.media_turma()
            case '4':
                print('Saindo...')
                break


menu()