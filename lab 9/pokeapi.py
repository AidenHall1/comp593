
import requests


#Gets poke info
#pram name = Pokemon name

def get_pokemon_info(name): 
    print("gettibg pokemon name", end='')

    url = "https://pokeapi.co/api/v2/pokemon/" + name 
    resp_message = requests.get(url)


    if resp_message.status_code == 200:
            print("It worked")
            return resp_message.json()

    else:
        print("Did not work", resp_message.status_code)
        return
#returns the list of the pokemon names
def get_list(limit=100, offset=0):
    url = 'https://pokeapi.co/api/v2/pokemon'

    params = {
        'limit' : limit,
        'offset' : offset
    }

    resp_messag = requests.get(url, params=params)

    if resp_messag.status_code == 200:

        dict = resp_messag.json()

        return [p['name']for p in dict['results']]

    else: 
       
        print("Did not work", resp_messag.status_code)
        return
#dictonry to grab the url for the photos
def get_poke_image_url(name):
    poke_dict = get_pokemon_info(name)
    if poke_dict:
        return poke_dict['sprites']['other']['official-artwork']['front_default']
