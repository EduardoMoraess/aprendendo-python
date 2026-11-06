class Carro:
    def __init__(self):
        self.velocidade = 0
    def acelerar(self):
        if self.velocidade < 120:
            self.velocidade += 10

            if self.velocidade > 120:
                self.velocidade = 120
carro1 = Carro()
carro1.acelerar()
print(carro1.velocidade)
