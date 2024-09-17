import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '28ea412c50330265f417602886397e35'
HEADER = {'Content-Type' : 'application/json','trainer_token' :TOKEN}

body_create = {
    "name": "Winter",
    "photo_id": 1
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create)
print(response_create.text)'''

body_change = {
    "pokemon_id": '71647',
    "name": "Gridalo",
    "photo_id": 2
}

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)
print(requests)'''

body_add = {
    "pokemon_id": "71647"
}
response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)

print(response_add)
print(response_add.text)



