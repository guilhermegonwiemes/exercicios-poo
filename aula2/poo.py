# classe estudante, chamada pela função cadastrar_estudante
class Estudante:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        estudantes.append(self)

    #função que calcula a media de cada estudante, chamada pela função situacao e listar
    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    # função que define a situação de cada estudante, chamada pela função listar
    def situacao(self):
        media = self.calcular_media()
        if media >= 6:
            return 'Aprovado'
        elif media >= 4:
            return 'Recuperação'
        else:
            return 'Reprovado'

    # função que lista todos os estudantes cadastrados, chamada pelo menu
    def listar():
        if len(estudantes) == 0:
            print('Nenhum estudante cadastrado.')
            return
        print(f'\n{'NOME':<16}{'N1':<7}{'N2':<7}{'MÉDIA':<8}{'SITUAÇÃO':<14}')
        for estudante in estudantes:
            print(f'{estudante.nome:<16}{estudante.nota1:<7}{estudante.nota2:<7}{estudante.calcular_media():<8.1f}{estudante.situacao():<14}')

    # função que calcula a média da turma, chamada pelo menu
    def media_turma():
        if len(estudantes) == 0:
            print('Nenhum estudante cadastrado.')
            return

        for estudante in estudantes:
            soma = sum(estudante.calcular_media() for estudante in estudantes)
            media = soma / len(estudantes)
        print(f'\nMédia da turma: {media:.1f}')

# array de estudantes para usar quando precisar dar for em todos os estudantess
estudantes = []

# função que cadastra um estudante, chama a classe e é chamada pelo menu
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

#função que chama o menu e inicia o programa
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