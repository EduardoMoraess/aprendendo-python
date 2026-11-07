class Animal:
    def __init__(self,idade):
        self.idade = idade
class Cachorro(Animal):
    def fase_vida(self):

        if self.idade <2:
            print('filhote')
        else:
            print('adulto')
meu_cachorro = Cachorro(5)
meu_cachorro.fase_vida()
