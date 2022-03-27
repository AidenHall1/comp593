import requests 
from sys import argv 


def main():
    poke_name = argv[1]
    poke_info = get_poke_info(poke_name)

    if poke_info:
       poke_name = get_poke_strings(poke_info) 
    
       paste_URL = post_pastebin(poke_name[0], poke_name[1], poke_ability[2])
      
       print(paste_URL)
   
def get_poke_strings(poke_name):
    
    title = "Name: " + str(poke_name["name"])
    body_text = "ID: " + str(poke_name['id'])
    body_text += " Weight: " + str(poke_name['weight'])
    
    
    for poke_info in poke_name['abilities']:
        poke_ability = ""   
        poke_ability += poke_name['ability']['name'] + "\n"
        poke_ability = poke_ability[:-1] 
        return(title, body_text, poke_ability)
    
    
    
    
    


    



def get_poke_info(poke_name):
    print("For filling your request...")
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + poke_name)

    if response.status_code == 200:
       print('We are groovy' , response.status_code )
       return response.json()
        
    else: 
        print('We are not groovy', resp_msg.status_code)
        return 
        
def post_pastebin(title, body_text): 
    print("Uploading now...")
    
    params = {
        'api_dev_key': "_aqfohHq7O2cDcjsZ2UP7R4e7-i0OPDi",
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        #'poke_ability': poke_ability
       
        }
        
    URL = 'https://pastebin.com/api/api_post.php'
    response = requests.post(URL, data=params)
        
    if response.status_code == 200: 
       print('It worked')
       return response.text
    else:
        print('did not work', response.status_code)
        return response.status_code
main()
