from ast import Pass
from cProfile import label
from optparse import Values
from tkinter import *
from tkinter import ttk
import os
import sys
import ctypes
from pokeapi import get_list, get_poke_image_url
import requests




def main():


#sets the window and the tool bar picture
    scirpt_dir = sys.path[0] 
    image_dir = os.path.join(scirpt_dir, 'images')
    if not os.path.isdir(image_dir):
        os.makedirs(image_dir)
    
    root = Tk()
    root.title('poke Image Viewer')
    myapid = 'comp593.PokemonImageViewer'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myapid)
    root.iconbitmap(os.path.join(scirpt_dir, 'Master-Ball.ico'))
    root.columnconfigure(0, weight =1)
    root.rowconfigure(0, weight=1)
    root.minsize(400, 400)
    root.geometry('600x600')

#set the sizing of the picture
    frame = ttk.Frame(root)
    frame.grid(sticky=(N,S,E,W))
    frame.columnconfigure(0, weight =1)
    frame.rowconfigure(0, weight=80)
    frame.rowconfigure(1, weight=10)
    frame.rowconfigure(2, weight=10)

    #puts another picture in the window 
    image_name = PhotoImage(file=os.path.join(scirpt_dir, 'ball.png'))
    label_image = Label(frame, image=image_name)
    label_image.grid(row=0, column=0, padx=10, pady=10)

    #sets up the combobox
    poke_list = get_list(limit=1000)
    poke_list.sort()
    box_selection = ttk.Combobox(frame, values=poke_list, state='readonly')
    box_selection.set('Select a pokemon :)')
    box_selection.grid(row=1, column=0)

    #gives functionality to the combobox
    def handle_box(event):
        Poke_name = box_selection.get()
        image_url = get_poke_image_url(Poke_name)
        image_path = os.path.join(image_dir, Poke_name + '.png')

        if downlaod_img(image_url, image_path):
            image_name['file'] = image_path
            button_set_desktop.state(['!disabled'])





    box_selection.bind('<<ComboboxSelected>>', handle_box)
    #gives the box an exubatble 
    def butten_clicked():
        Poke_name = box_selection.get()
       
        image_path = os.path.join(image_dir, Poke_name + '.png')

        set_desktop(image_path)




    button_set_desktop = ttk.Button(frame, text='Set as Desktop image' ,command= butten_clicked)
    button_set_desktop.state(['disabled'])
    button_set_desktop.grid(row=2, column=0)



    root.mainloop()
    #sets the background
def set_desktop(path):

    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

    except:
        print("erroe has orrcurredddd")

    
    
#downloads the image and stes the path

def downlaod_img(url, path):

    if os.path.isfile(path):
        return path

    resp_mesg = requests.get(url)
    if resp_mesg.status_code == 200:
        try:

            img_data = resp_mesg.content
            with open(path, 'wb') as fp:
              fp.write(img_data)
            return path

        except:
            return

    else:
        print('failed to dowmlaod')
        print(resp_mesg.status_code)





main()

