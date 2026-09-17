import qrcode
from pathlib import Path


def gerar_qrcode():
    texto = input('Digite o texto ou link: ').strip()

    if not texto:
        print('Erro: você precisa informar um texto ou link.')
        return

    arquivo = Path('meu_qrcode.png')

    qr_code = qrcode.make(texto)
    qr_code.save(arquivo)

    print(f'QR Code gerado com sucesso!')
    print(f'Arquivo salvo em: {arquivo.resolve()}')

if __name__ == '__main__':
    gerar_qrcode()
