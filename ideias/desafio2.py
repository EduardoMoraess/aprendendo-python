from InquirerPy.resolver import prompt

perguntas= [
    {
        "type": "list",
        "name": "nivel",
        "message": "Qual seu nivel em python?",
        "choices": ["vista", "intermediario", "senior"]
    }
]

resultado = prompt(perguntas)
nivel = resultado["nivel"]

if nivel == "vista":
    print("Boa sorte nessa jornada") 
    valor = float(input("digite o valor:"))
    desconto = valor * 0.95
    print(desconto)

elif nivel == "intermediario":
    print('Estude Poo')
elif nivel == "senior":
    print('Estude arquitetura, testes e otimização')
