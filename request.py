import requests

"""
Del api de pokemon cuya documentación se encuentra en la pagina https://pokeapi.co/, realiza las siguientes instrucciones:

Crea una función en python que consuma el siguiente servicio: 

API GET https://pokeapi.co/api/v2/type/{name}/ 

donde "name" es un parámetro de la función que va ser el tipo de pokemon y la función va regresar la información del tipo 
(documentación del api https://pokeapi.co/docs/v2.html/#types).

"""

def getType(name: str):
    url = 'https://pokeapi.co/api/v2/type/' + name
    res = requests.get(url)
    if res:
        return print(res, res.json())
    else:
        print(res, 'Por favor utilice un type existente')

"""
Modificar la función anterior para que la respuesta solo regrese el arreglo "pokemon"
"""
def getTypePokemon(name: str):
    url = 'https://pokeapi.co/api/v2/type/' + name
    res = requests.get(url)
    if res:
        pokemon = res.json()
        return print(res, pokemon['pokemon'])
    else:
        print(res, 'Por favor utilice un type existente')


"""
Modificar nuevamente la función anterior, esta vez para obtener solo los pokemons que empiecen con la letra "s"
"""
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

"""
Escribe una función en python que reciba un número y regrese el número primo posterior más cercano.

"""
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
