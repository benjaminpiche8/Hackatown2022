import json
import requests
from PIL import Image

### Current conditions ###

def get_current_icon() :
    with open('database\database_current.json', 'r') as outfile :
        data = json.load(outfile)
        url = data['condition']['icon']
        image = Image.open(requests.get('https:' + url, stream = True).raw)
        image.show()
        return image

def get_current_condition() :
    with open('database\database_current.json', 'r') as outfile :
        data = json.load(outfile)
        return data['condition']['text']

def get_current_raw_temp(system) :
    with open('database\database_current.json', 'r') as outfile :
        data = json.load(outfile)
        if system == 'c' :
            return data['temp_c']
        else :
            return data['temp_f']

def get_current_feelslike_temp(system) :
    with open('database\database_current.json', 'r') as outfile :
        data = json.load(outfile)
        if system == 'c' :
            return data['feelslike_c']
        else :
            return data['feelslike_f']


### Forecast conditions ###

def get_forecast_icon() :
    with open('database\database_forecast.json', 'r') as outfile :
        data = json.load(outfile)
        values = list(data.values())
        for sublist in values :
            for dict in sublist :
                print(dict, '\n', '\n')
        #    print(date, '\n', '\n')
        #print(type(items), '\n')
        #url = data['condition']['icon']
        #image = Image.open(requests.get('https:' + url, stream = True).raw)
        #image.show()
        #return image

if __name__ == "__main__" :
    # print(type(get_forecast_icon()), get_forecast_icon())
    get_forecast_icon()