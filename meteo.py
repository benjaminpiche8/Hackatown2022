import json
import requests
from PIL import Image

### Current conditions ###

def get_current_icon() :
    with open('database\database_current.json', 'r') as outfile :
        data = json.load(outfile)
        url = data['condition']['icon']
        elements = url.split('/')
        path = 'icons/' + elements[3] + '/' + elements[4] + '/' + elements[5] + '/' + elements[6]
        return path
        #image = Image.open(requests.get('https:' + url, stream = True).raw)
        #image.show()
        #return image

def get_current_condition() :
    with open('database\database_current.json', 'r') as outfile :
        data = json.load(outfile)
        return data['condition']['text']

def get_current_raw_temp(system) : # parameter format string 'c' or 'f'
    with open('database\database_current.json', 'r') as outfile :
        data = json.load(outfile)
        if system == 'c' :
            return data['temp_c']
        else :
            return data['temp_f']

def get_current_feelslike_temp(system) : # parameter format string 'c' or 'f'
    with open('database\database_current.json', 'r') as outfile :
        data = json.load(outfile)
        if system == 'c' :
            return data['feelslike_c']
        else :
            return data['feelslike_f']


### Daily forecast conditions ###

def get_daily_forecast_icon(date) : # parameter format string 'XXXX-XX-XX'
    with open('database\database_forecast.json', 'r') as outfile :
        data = json.load(outfile)
        values = list(data.values())
        for sublist in values :
            for day in sublist :
                if day['date'] == date :
                    url = day['day']['condition']['icon']
                    elements = url.split('/')
                    path = 'icons/' + elements[3] + '/' + elements[4] + '/' + elements[5] + '/' + elements[6]
                    return path
                    

def get_daily_forecast_condition(date) : # parameter format string 'XXXX-XX-XX'
    with open('database\database_forecast.json', 'r') as outfile :
        data = json.load(outfile)
        values = list(data.values())
        for sublist in values :
            for day in sublist :
                if day['date'] == date :
                    return day['day']['condition']['text']

def get_daily_forecast_raw_temp(system, metric, date) : # parameter format string 'c' or 'f', string 'max' or 'min' and string 'XXXX-XX-XX'
    with open('database\database_forecast.json', 'r') as outfile :
        data = json.load(outfile)
        values = list(data.values())
        for sublist in values :
            for day in sublist :
                if day['date'] == date :
                    if system == 'c' and metric == 'max' :
                        return day['day']['maxtemp_c']
                    elif system == 'c' and metric == 'min' :
                        return day['day']['mintemp_c']
                    elif system == 'f' and metric == 'max' :
                        return day['day']['maxtemp_f']
                    else :
                        return day['day']['mintemp_f']

def will_it_snow(date) : # parameter format string 'XXXX-XX-XX'
    with open('database\database_forecast.json', 'r') as outfile :
        data = json.load(outfile)
        values = list(data.values())
        for sublist in values :
            for day in sublist :
                if day['date'] == date :
                    if day['day']['daily_will_it_snow'] == 0 :
                        return False
                    else :
                        return True

def will_it_rain(date) : # parameter format string 'XXXX-XX-XX'
    with open('database\database_forecast.json', 'r') as outfile :
        data = json.load(outfile)
        values = list(data.values())
        for sublist in values :
            for day in sublist :
                if day['date'] == date :
                    if day['day']['daily_will_it_rain'] == 0 :
                        return False
                    else :
                        return True

# if __name__ == "__main__" :