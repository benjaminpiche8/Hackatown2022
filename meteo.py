import json
import requests
from PIL import Image

def current_meteo_type() :
    with open('database\database_current.json', 'r') as outfile :
        data = json.load(outfile)
        url = data['condition']['icon']
        image = Image.open(requests.get('https:' + url, stream = True).raw)
        image.show()
        return image

if __name__ == "__main__" :
    current_meteo_type()