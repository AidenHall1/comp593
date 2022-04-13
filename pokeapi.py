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
        