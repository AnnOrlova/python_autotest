import requests

token = '691f01cc9a7db38744518545d92395e8'
response = requests.post('https://pokemonbattle.me:9104/trainers/reg', 
              headers = {'Content-Type': 'application/json'}, 
              json= {
    "trainer_token": token,
    "email": "anna-orlova-97@mail.ru",
    "password": "A12345"
})
print(response.text)

response_confirm = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email',
                         headers = {'Content-Type': 'application/json'},
                         json = {"trainer_token": token})
print(response_confirm.text)

create_pokemon_response = requests.post('https://pokemonbattle.me:9104/pokemons', 
                                        headers = {'Content-Type': 'application/json',
                                                   "trainer_token": token},
                                        json = {'name':'Eve',
                                                'photo':'https://dolnikov.ru/pokemons/albums/133.png'})
print(create_pokemon_response.text)

change_name_response = requests.put('https://pokemonbattle.me:9104/pokemons',
                                    headers = {'Content-Type': 'application/json',
                                                "trainer_token": token},
                                    json = {"pokemon_id": '6256',
                                            "name": "Eevee",
                                            'photo':'https://dolnikov.ru/pokemons/albums/133.png'})
print(change_name_response.text)

add_pokeball_response = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball',
                                      headers = {'Content-Type': 'application/json',
                                                "trainer_token": token},
                                        json = {'pokemon_id': '6256'})
print(add_pokeball_response.text)