class Gerador:
    def __init__(self, nome, potencia, capacidade_energia, tamanho_tanque):
        self.__nome = nome
        self.__potencia = potencia
        self.__capacidade_energia = capacidade_energia
        self.__tamanho_tanque = tamanho_tanque
        self.__quantidade_combustivel = 0               # inicia com o tanque vazio
        self.__ligado = False                           # inicia desligado

    # Métodos Set não foram criados porque não são usados
    # as alterações dos atributos é feita pelos metodos especificos de abastecer, ligar, desligar

    # Métodos Get
    def get_nome(self):
        return self.__nome

    def get_potencia(self):
        return self.__potencia

    def get_capacidade_energia(self):
        return self.__capacidade_energia

    def get_tamanho_tanque(self):
        return self.__tamanho_tanque

    def get_quantidade_combustivel(self):
        return self.__quantidade_combustivel

    def get_ligado(self):
        return self.__ligado

    # acionamento do gerador
    def ligar(self):
        if self.__quantidade_combustivel >= 50:             # Só liga se tiver 50 litros ou mais de combustivel
            self.__ligado = True                            # liga o gerador
            # consome 50 litros de combustivel
            self.__quantidade_combustivel -= 50
            print(self.__nome, "foi ligado com sucesso")
        else:
            print(self.__nome, "não pode ser ligado por falta de combustível")

    def desligar(self):
        self.__ligado = False                            # desliga o gerador
        print(self.__nome, "foi desligado com sucesso")

    # abastecer o tanque do gerador
    def abastecer(self, quantidade):
        # Verifica se não ultrapassa a capacidade do tanque
        if self.__quantidade_combustivel + quantidade <= self.__tamanho_tanque:
            # incrementa a quantidade de combustivel
            self.__quantidade_combustivel += quantidade
            print(self.__nome, "foi abastecido com sucesso")
        else:
            print("Não é possível abastecer essa quantidade de combustível")

    # Exibir os detalhes do gerador
    def exibir_detalhes(self):
        print("DETALHES DO GERADOR:")
        print("Nome:", self.__nome)
        print("Potência::", self.__potencia)
        print("Capacidade de geração de energia:", self.__capacidade_energia)
        print("Tamanho do Tanque:", self.__tamanho_tanque)
        print("Status: ", self.__ligado)


# ========================= FUNÇÕES AUXILIARES ==================================

# exibe o menu principal e retorna a opção escolhida
def menu():
    print("1 - Acionamento manual de gerador")
    print("2 - Status dos geradores")
    print("3 - Status dos tanques de combustível")
    print("4 - Abastecer tanque de combustível")
    print("5 - Detalhes do gerador")
    print("6 - Sair")
    opcao = int(input("Escolha a opçao: "))
    return opcao


# recebe o gerador e verifica se precisa abastecer. Exibe a mensagen correspondente
def exibir_quantidade_combustivel(gerador):
    if gerador.get_quantidade_combustivel() < gerador.get_tamanho_tanque() * 0.20:
        print(gerador.get_quantidade_combustivel(), "/",
              gerador.get_tamanho_tanque(), "litros (ABASTECER)")
    else:
        print(gerador.get_quantidade_combustivel(), "/",
              gerador.get_tamanho_tanque(), "litros")


# recebe o gerador e verifica o status, Exibe mensagem corresponde (ligado ou desligado)
def exibir_status(gerador):
    if gerador.get_ligado():
        print(gerador.get_nome(), "- LIGADO")
    else:
        print(gerador.get_nome(), "- DESLIGADO")


# recebe o nome do gerador e retorna o objeto correspondente. Se nao existir, retorna None
def buscar_gerador(nome):
    if nome == g1.get_nome():
        return g1
    elif nome == g2.get_nome():
        return g2
    elif nome == g3.get_nome():
        return g4
    elif nome == g4.get_nome():
        return g4
    else:
        return None


# ========================= PROGRAMA PRINCIPAL ==================================

# criação dos objetos (geradores)
g1 = Gerador("G1", 85, 7000, 400)
g2 = Gerador("G2", 85, 7000, 400)
g3 = Gerador("G3", 85, 7000, 400)
g4 = Gerador("G4", 85, 7000, 400)

opcao = 0
while opcao != 6:
    opcao = menu()
    if opcao == 1:
        nome = input("Informe o nome do gerador: ")
        # busca o gerador de acordo com o nome
        gerador = buscar_gerador(nome)
        if gerador is not None:
            if gerador.get_ligado() is True:            # verifica o status do gerador
                print("Gerador está Ligado. Deseja Desligar?")
            else:
                print("Gerador está Desligado. Deseja Ligar?")
            print("1 - Sim")
            print("2 - Não")
            escolha = int(input("Escolha a opção: "))
            if escolha == 1 and gerador.get_ligado() is True:       # se estiver ligado, desliga
                # se for o G1, só desliga se nao tiver outro gerador ligado
                if gerador.get_nome() == g1.get_nome():
                    if g2.get_ligado() is False and g2.get_ligado() is False and g3. get_ligado() is False:
                        gerador.desligar()
                    else:
                        print(
                            "Não é possivel desligar G1 porque outros geradores estão ligados")
                else:
                    gerador.desligar()
            elif escolha == 1 and gerador.get_ligado() is False:    # se estiver desligado, liga
                if gerador.get_nome() == g1.get_nome():             # quando for o G1, liga
                    gerador.ligar()
                else:
                    if g1.get_ligado() is True:                     # quando nao for o G1, verifica se G1 ja ta ligado
                        gerador.ligar()
                    else:
                        print(gerador.get_nome(),
                              "não pode ser ligado porque G1 está desligado")
            elif escolha == 2:
                pass                        # não faz nada
            else:
                print("Opção inválida")
        else:
            print("Nome do Gerador inválido")

    elif opcao == 2:
        print("STATUS DOS GERADORES:")
        exibir_status(g1)
        exibir_status(g2)
        exibir_status(g3)
        exibir_status(g4)
    elif opcao == 3:
        print("STATUS DOS TANQUES:")
        exibir_quantidade_combustivel(g1)
        exibir_quantidade_combustivel(g2)
        exibir_quantidade_combustivel(g3)
        exibir_quantidade_combustivel(g4)
    elif opcao == 4:
        nome = input("Informe o nome do gerador: ")
        # busca o gerador de acordo com o nome
        gerador = buscar_gerador(nome)
        if gerador is not None:
            quantidade = int(input("Quantidade de Litros de Combustível: "))
            gerador.abastecer(quantidade)
        else:
            print("Nome do Gerador inválido")
    elif opcao == 5:
        nome = input("Informe o nome do gerador: ")
        # busca o gerador de acordo com o nome
        gerador = buscar_gerador(nome)
        if gerador is not None:
            gerador.exibir_detalhes()
        else:
            print("Nome do Gerador inválido")
    elif opcao == 6:
        print("Final da execução")
    else:
        print("Opção inválida")