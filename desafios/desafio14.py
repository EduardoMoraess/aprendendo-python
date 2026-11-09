class Gato:
    def emitir_som(self):
        print('miau')
class Cachorro:
    def emitir_som(self):
        print('auau')

gato = Gato()
cachorro = Cachorro()

animais = [gato, cachorro]

for animal in animais:
    animal.emitir_som()
