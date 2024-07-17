from PIL import Image
import pandas as pd
import requests
import re
# from bs4 import BeautifulSoup
# from os.path import basename

# ------------------------------------------------ CREAR LA IMAGEN

# url = 'https://cdn.7tv.app/emote/60fd7ed62598fc5c9bee9295/4x.webp'
# nombre_local_imagen = "go.png"
# imagen = requests.get(url).content

# with open(nombre_local_imagen, 'wb') as file:
#     file.write(imagen)

#-------------------------------------------------



# Convertidor de .wedp a Gif

# im = Image.open('4x668915fcfbe3f7b7cf0940cc.webp')

# im.save('4x668915fcfbe3f7b7cf0940cc.gif', 'gif', save_all=True)



stickers_file = 'stickers.csv'

df = pd.read_csv(stickers_file)

links_search = []

links = df['Links'].tolist()

for link in links:
    original_link = link
    cdn_domain = 'cdn.7tv.app/emote'

    modifications_link = original_link.replace('https://7tv.app/emotes', f'https://{cdn_domain}')
    modifications = f'{modifications_link}/4x.webp'
    links_search.append(modifications)

for link in links_search: 
    img = requests.get(link).content
    regex = r"\/([^\/]+)\/"
    coincidence = re.findall(regex, link)
    with open(f"{coincidence[-1]}.webp", 'wb') as file:
        file.write(img)
        # print(parte_deseada)
    
    
    
    
    
    # with open(img, 'wb') as file:
    #     file.write(file)

# for dw in links_search:
#     img = requests.get(dw).content
#     with open(dw, 'wb') as file:
#         file.write(file)