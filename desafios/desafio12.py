class Tv:
    def __init__(self):
        self.volume = 0
    def aumentar_volume(self):
        if self.volume < 10:
            self.volume += 1
tv1 = Tv()

while tv1.volume <10:
    tv1.aumentar_volume()
print(f'o volume atual da TV é {tv1.volume}')
