from tkinter import * 
from tkinter import ttk
from webbrowser import get
from pokeapi import get_pokemon_info




def main():
    #window creation
    root = Tk()
    root.title("Pokemon Info GUI")
    root.iconbitmap("Master-ball.ico")
   

    #craeting frames for the window 
    frame_input = ttk.Frame(root)
    frame_input.grid(row=0, column=0, columnspan=3)

    frame_info =ttk.LabelFrame(root, text='Info')
    frame_info.grid(row=1, column=0)

    frame_stats = ttk.LabelFrame(root, text='Stats')
    frame_stats.grid(row=1, column=1)

    

#displays widgets in the input frame 
    lable_name = ttk.Label(frame_input, text='Pokemon Name: ')
    lable_name.grid(row=0, column=0, padx=10, pady=10)

    entry_name = ttk.Entry(frame_input)
    entry_name.grid(row=0, column=1, padx=10, pady=10 )

    def button_click():
        #get the poke info from the api
        pokemon_name = entry_name.get()
        poke_dict = get_pokemon_info(pokemon_name)
        #display the values 
        if poke_dict:
            
            label_height_value['text'] = str(poke_dict['height']) + ' dm'
            label_weight_value['text'] = str(poke_dict['weight']) + ' Hg'
            progress_hp['value'] = poke_dict['stats'][0]["base_stat"]
            progress_attack['value'] = poke_dict['stats'][1]["base_stat"]
            progress_deffence['value'] = poke_dict['stats'][2]["base_stat"]
            progress_special_attack['value'] = poke_dict['stats'][3]['base_stat']
            progress_special_Deffence['value'] = poke_dict['stats'][4]['base_stat']
            progress_speed['value'] = poke_dict['stats'][5]['base_stat']
            type_list = [t['type']['name']for t in poke_dict['types']]
            label_type_value['text'] = ', '.join(type_list)




      


       

    button_info = ttk.Button(frame_input, text='Search info', command=button_click)
    button_info.grid(row=0, column=2, padx=10, pady=10)


#display widegts in info frame
#sets up the height 
    label_height = ttk.Label(frame_info, text='Height: ')
    label_height.grid(row=100, column=100)


    label_height_value = ttk.Label(frame_info, width=15)
    label_height_value.grid(row=100, column=200)
    
   #sets up the types
    label_type = ttk.Label(frame_info, text='Type: ')
    label_type.grid(row=300, column=100)


    label_type_value = ttk.Label(frame_info, width=15)
    label_type_value.grid(row=300, column=200)
    #sets up the weight
    label_weight = ttk.Label(frame_info, text='Weight: ')
    label_weight.grid(row=400, column=100)


    label_weight_value = ttk.Label(frame_info, width=15)
    label_weight_value.grid(row=400, column=200)


    #display the widgtes in the stats frame

    label_health = ttk.Label(frame_stats, text='HP: ')
    label_health.grid(row=100, column=100)
    progress_hp = ttk.Progressbar(frame_stats, length=200, maximum=255)
    progress_hp.grid(row=100, column=200)

    label_attack = ttk.Label(frame_stats, text='Attack: ')
    label_attack.grid(row=300, column=100)
    progress_attack = ttk.Progressbar(frame_stats, length=200, maximum=255)
    progress_attack.grid(row=300, column=200)

    label_deffence = ttk.Label(frame_stats, text='Deffence: ')
    label_deffence.grid(row=400, column=100)
    progress_deffence = ttk.Progressbar(frame_stats, length=200, maximum=255)
    progress_deffence.grid(row=400, column=200)
    
    label_special_attack = ttk.Label(frame_stats, text='Special Attack: ')
    label_special_attack.grid(row=500, column=100)
    progress_special_attack = ttk.Progressbar(frame_stats, length=200, maximum=255)
    progress_special_attack.grid(row=500, column=200)
    
    label_special_Deffence = ttk.Label(frame_stats, text='Special Deffence: ')
    label_special_Deffence.grid(row=600, column=100)
    progress_special_Deffence = ttk.Progressbar(frame_stats, length=200, maximum=255)
    progress_special_Deffence.grid(row=600, column=200)
    
    label_speed = ttk.Label(frame_stats, text='Speed: ')
    label_speed.grid(row=700, column=100, padx=5)
    progress_speed = ttk.Progressbar(frame_stats, length=200, maximum=255)
    progress_speed.grid(row=700, column=200)
    
    def random_button():
        button_inf = ttk.Button(frame_info, text='Random Stat', command=random_button)
        button_inf.grid(row=1,column=1)

    
    
    root.mainloop()




main()    