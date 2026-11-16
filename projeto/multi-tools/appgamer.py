class Jogador:
    def __init__(self, nome, hp):
        self.nome = nome
        self.hp = hp
        self.danobase = 0
        self.agilidadebase = 0

qj = int(input('Quantos jogadores na partida :>'))
jogadores : list[Jogador] = []
hp = int(input("HP dos jogadores :>"))

for i in range(qj):
    nome = str(input(f"Nome do jogador:> {i+1}"))
    jogadores.append(Jogador(nome,hp))
for i in range(qj):
    print(f'ola jodagores:> {jogadores[i].nome}')
