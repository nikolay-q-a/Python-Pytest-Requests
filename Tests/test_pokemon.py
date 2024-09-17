import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '28ea412c50330265f417602886397e35'
HEADER = {'Content-Type' : 'application/json','trainer_token' :TOKEN}
TRAINER_ID = '8434'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', headers = HEADER, params ={'trainer_id' : TRAINER_ID} )
    assert response.status_code == 200   
   