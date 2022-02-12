import requests
import json

def build_api_url(location, num_days) :
    base_url = 'https://api.weatherapi.com/v1'
    request = '/forecast.json'
    api_key = 'key=586e03d395324a3583813301'  
    date = '221202' # will it change?
    query = 'q=' + location  # add getLocation function
    days = 'days=' + str(num_days)
    aqi = 'aqi=no'
    alerts = 'alerts=yes'
    
    return base_url + request + '?' + api_key + date + '&' + query + '&' + days + '&' + aqi + '&' + alerts

def call_api(api_url) :
    response = requests.get(api_url)
    return response

def write_json(response) :
    json_data = json.loads(response.text)
    for key in json_data.keys() :
        with open('database_' + key + '.json', 'w') as outfile :
            json.dump(json_data[key], outfile)

if __name__ == "__main__" :
    data = call_api(build_api_url('Montreal', 3))
    write_json(data)