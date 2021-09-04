import requests


def getType(name: str):
    url = 'https://pokeapi.co/api/v2/type/' + name
    res = requests.get(url)
    if res:
        return print(res, res.json())
    else:
        print(res, 'Por favor utilice un type existente')


def getTypePokemon(name: str):
    url = 'https://pokeapi.co/api/v2/type/' + name
    res = requests.get(url)
    if res:
        pokemon = res.json()
        return print(res, pokemon['pokemon'])
    else:
        print(res, 'Por favor utilice un type existente')


def getTypePokemonWhitS(name: str):
    url = 'https://pokeapi.co/api/v2/type/' + name
    res = requests.get(url)
    if res:
        data = res.json()
        data_pokemon = data['pokemon']
        result = [pokemon for pokemon in data_pokemon if pokemon['pokemon']
                  ['name'].startswith("s")]
        return print(res, result)
    else:
        print(res, 'Por favor utilice un type existente')


def NumeroPrimoSiguiente(num: int):
    def primo(numero: int):
        for n in range(2, numero):
            if numero % n == 0:
                return False
        return True
    i = 1
    while not primo(num+i):
        i += 1
    return print(num+i)
