import requests 
import pytest 

def test_chek_status_code():
    response = requests.get('https://pokemonbattle.me:9104/trainers')
    assert response.status_code == 200

def test_check_string():
    response = requests.get('https://pokemonbattle.me:9104/trainers',
                            params = {'trainer_id': 3413})
    assert response.json()['trainer_name'] == 'Anna'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Anna')])

def test_check_parametrs(key, value):
    response = requests.get('https://pokemonbattle.me:9104/trainers',
                            params = {'trainer_id': 3413})
    assert response.json()[key] == value