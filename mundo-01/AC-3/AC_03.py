
class Gerador:
    def __init__(self, nome, potencia, capacidade, tanque):
        self.__nome = nome
        self.__potencia = potencia
        self.__capacidade = capacidade
        self.__tanque = tanque
        self.__status = 0
        self.__combustivel = 0

    def get_nome(self):
        return self.__nome

    def get_potencia(self):
        return self.__potencia

    def get_capacidade(self):
        return self.__capacidade

    def get_tanque(self):
        return self.__tanque

    def get_combustivel(self):
        return self.__combustivel

    def get_status(self):
        if self.__status == 1:
            return f"{self.__nome} Ligado\t\t\t"
        return f"{self.__nome} Desligado\t\t\t"

    def set_status(self):
        if self.__status == 1:
            self.__status = 0
        else:
            if (self.__nome != 'G1') and ('Desligado' in geradores[0].get_status()):
                return f'{self.__nome} não pode ser ligado por que G1 está desligado'
            if self.__combustivel < 50:
                return f'{self.__nome} não pode ser ligado por falta de combustível'
            self.__combustivel -= 50
            self.__status = 1
        return self.get_status()

    def set_combustivel(self, litros):
        if litros > 0 and type(litros) == int:
            if (self.__combustivel + litros) > self.__tanque:
                return f'O tanque não suporta mais {litros} litro(s)'
            else:
                self.__combustivel += litros
                return f'Combustível atualizado: {self.__combustivel}'
        else:
            return 'Os valores de abastecimento devem ser inteiros positivos'

    def auxilar_liga_desliga(self):
        if self.__status == 1:
            print(f'{self.__nome} está Ligado, deseja Desligar?')
        else:
            print(f'{self.__nome} está Desligado, deseja Ligar?')
        print(f'1 - Sim\n2 - Não')
        if input_escolhas(2) == 1:
            return self.set_status()

    def analisar_combustivel(self):
        if self.__combustivel / self.__tanque < 0.2:
            return f'{self.__combustivel}/{self.__tanque} litros\t\t(ABASTECER)'
        return f'{self.__combustivel}/{self.__tanque} litro(s)\t\t'


def menu_inicial():
    opcoes = []
    opcoes.append(["Acionamento manual de gerador", 'acionar'])
    opcoes.append(["Status dos geradores", 'status'])
    opcoes.append(["Status dos tanques de combustível", 'combustivel'])
    opcoes.append(["Abastecer tanque de combustível", 'abastecer'])
    opcoes.append(["Detalhes do gerador", 'detalhes'])
    opcoes.append(["Sair", 'sair'])
    print(f' {"-"*13}Menu Principal{"-"*13}')
    for index, opcao in enumerate(opcoes):
        print(index + 1, " - ", opcao[0])
    opcao = input_escolhas(len(opcoes))
    menu_opcao(opcoes[opcao - 1][0], opcoes[opcao - 1][1])


def menu_opcao(descricao, opcao):
    print(f' {"-"*3}{descricao}{"-"*3}')
    if opcao == 'acionar':
        gerador = procurar_gerador()
        if gerador:
            print(gerador.auxilar_liga_desliga(), '\t\t\t<-------')
    elif opcao == 'status':
        print('STATUS DOS GERADORES:', '\t\t\t<-------')
        for gerador in geradores:
            if 'Desligado' in gerador.get_status():
                print(f'{gerador.get_nome()} - Desligado', '\t\t\t<-------')
            else:
                print(f'{gerador.get_nome()} - Ligado', '\t\t\t<-------')
    elif opcao == 'combustivel':
        print('STATUS DOS GERADORES:')
        for gerador in geradores:
            print(gerador.analisar_combustivel(), '\t\t\t<-------')
    elif opcao == 'abastecer':
        gerador = procurar_gerador()
        if gerador:
            litros = ""
            while type(litros) != int:
                try:
                    litros = int(
                        input(f'Quantidade de Litros de Combustível: '))
                except Exception:
                    print('Digite apenas numeros inteiros')
            print(gerador.set_combustivel(litros), '\t\t\t<-------')
    elif opcao == 'detalhes':
        gerador = procurar_gerador()
        if gerador:
            print('STATUS DOS GERADORES:', '\t\t\t<-------')
            print(f'Nome: {gerador.get_nome()}')
            print(f'Potência: {gerador.get_potencia()}')
            print(
                f'Capacidade de geração de energia: {gerador.get_capacidade()}')
            print(f'Tamanho do Tanque: {gerador.get_tanque()}')
            print(f'Status: {gerador.get_status()}')
    elif opcao == 'sair':
        print('O programa será desligado.', '\t\t\t<-------')
        return
    menu_inicial()


def procurar_gerador():
    nome_gerador = input(f'Informe o Nome do Gerador: ')
    for gerador in geradores:
        if gerador.get_nome() == nome_gerador:
            return gerador
    print(f"Gerador não encontrado", '\t\t\t<-------')


def input_escolhas(alternativas, opcao=0):
    while type(opcao) != int or not (0 < opcao <= alternativas):
        try:
            opcao = int(input(f'Escolha uma opção entre 1 e {alternativas}: '))
        except Exception:
            print(f"Escolha uma opção entre 1 e {alternativas}: ")
    return opcao


geradores = []
geradores.append(Gerador('G1', 150, 10000, 700))
geradores.append(Gerador('G2', 85, 7000, 400))
geradores.append(Gerador('G3', 85, 7000, 400))
geradores.append(Gerador('G4', 50, 5000, 300))
geradores[0].set_combustivel(100)
geradores[0].set_status()
menu_inicial()
