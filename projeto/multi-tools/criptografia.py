from cryptography.fernet import Fernet


chave = Fernet.generate_key()
print("Chave", chave.decode())

fernet = Fernet(chave)

mensagem = input("Digite sua mensagem:=>")
mensagem_cifra = fernet.encrypt(mensagem.encode("utf-8"))
print("Cifra:=>", mensagem_cifra.decode())
