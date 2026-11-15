import requests

nome_pokemon = "pikachu"
url =  f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"
resposta = requests.get(url)


if resposta.status_code == 200:
    pokemon = resposta.json()

    print(f'Nome: {pokemon["name"]}')
    print(f'Altura: {pokemon["height"]}')
else:
    print('Não conseguimos obter as infromações')
