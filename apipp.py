from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return 'Minha primeira API!'

@app.get("/pokemon/{nome}")
def buscar_pokemon(nome:str):
    return {
        'pokemon': nome,
        'tipo': 'eletrico'
    }
