import requests

def savePokemon():
    url = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
    response = requests.get(url)
    data = response.json()
    poke_data = []
    poke_dict = {}
    pokemon = data['forms'][0]['name']
    poke_dict[pokemon] = {
        'name' : data['forms'][0]['name'],
        'abilities' : data['abilities'][0]['ability']['name'],
        'base_exp' : data['base_experience'],
        'sprite' : data['sprites']['front_shiny'],
        'attack' : data['stats'][0]['base_stat'],
        'hp' : data['stats'][1]['base_stat'],
        'defense' : data['stats'][2]['base_stat']
        }
    
    poke_data.append(poke_dict)
    return poke_data