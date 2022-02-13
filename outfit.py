import meteo as mt
from datetime import date
import random

# def create_wardrobe() :
#     wardrobe = {
#         'tops' : [],
#         'bottoms' : [],
#         'footwear' : [],
#         'accessories' : []
#     }

#     return wardrobe


def short_term_recommandation_top(sex) :
    c_raw_temp = mt.get_current_raw_temp('c')
    c_feelslike_temp = mt.get_current_feelslike_temp('c')
    c_precip = mt.get_current_precip()

    possibilities_men = []
    possibilities_women = []

    if c_raw_temp <= -5 or c_feelslike_temp <= -10 :
        possibilities_men.append('long sleeves', 'hoodie', 'winter coat')
        possibilities_women.append('long sleeves', 'hoodie', 'light coat')

    if (-5 < c_raw_temp <= 15) or (-10 < c_feelslike_temp <= 20) :
        possibilities_men.append('long sleeves', 'hoodie', 'light coat')
        possibilities_women.append('long sleeves', 'hoodie', 'light coat')

    if (c_raw_temp > 15 or c_feelslike_temp > 20) and sex == 'm':
        possibilities_men.append('t-shirt')

    if (c_raw_temp > 15 or c_feelslike_temp > 20) and sex == 'w':
        possibilities_women.append('t-shirt', 'dress')

    if c_precip > 0 :
        possibilities_men.append('rain coat')
        possibilities_women.append('rain coat')

    if sex == 'm' :
        return random.choice(possibilities_men)
    else :
        return random.choice(possibilities_women)

def short_term_recommandation_bottom(sex) :
    c_raw_temp = mt.get_current_raw_temp('c')
    c_feelslike_temp = mt.get_current_feelslike_temp('c')
    c_precip = mt.get_current_precip()

    possibilities_men = []
    possibilities_women = []

    if c_raw_temp < 15 :
        possibilities_men.append('pants')

    if c_raw_temp >= 15 and sex == 'm' :
        possibilities_men.append('shorts')

    if c_raw_temp < 15 and sex == 'w' :
        possibilities_women.append('pants', 'leggings')
    
    if c_raw_temp > 15 and sex == 'w' :
        possibilities_women.append('shorts', 'skirt')

    if sex == 'm' :
        return random.choice(possibilities_men)
    else :
        return random.choice(possibilities_women)









def long_term_possibilities(f_raw_temp, f_rain, f_snow, sex) :
    possibilities = create_wardrobe()

    if f_raw_temp < -5 and sex == 'm' :
        possibilities['tops'].append('long sleeves', 'hoodie', 'winter coat')
        possibilities['bottoms'].append('pants')
        possibilities['footwear'].append('boots')
        possibilities['accessories'].append('hat', 'scarf', 'gloves')

    if (-5 <= f_raw_temp < 15) and sex == 'm' :
        possibilities['tops'].append('long sleeves', 'hoodie', 'light coat')
        possibilities['bottoms'].append('pants')
        possibilities['footwear'].append('boots')
        possibilities['accessories'].append('hat', 'scarf', 'gloves')

    if f_raw_temp > 15 and sex == 'm' :
        possibilities['tops'].append('t-shirt')
        possibilities['bottoms'].append('shorts')
        possibilities['footwear'].append('casual shoes', 'running shoes')
        possibilities['accessories'].append('cap')

    if f_raw_temp < -5 and sex == 'w' :
        possibilities['tops'].append('long sleeves', 'hoodie', 'winter coat')
        possibilities['bottoms'].append('pants', 'leggings')
        possibilities['footwear'].append('boots')
        possibilities['accessories'].append('hat', 'scarf', 'gloves')

    if (-5 <= f_raw_temp < 15) and sex == 'w' :
        possibilities['tops'].append('long sleeves', 'hoodie', 'light coat')
        possibilities['bottoms'].append('pants', 'leggings')
        possibilities['footwear'].append('casual shoes')
        possibilities['accessories'].append('hat', 'cap')
    
    if f_raw_temp > 15 and sex == 'w' :
        possibilities['tops'].append('t-shirt', 'dress')
        possibilities['bottoms'].append('shorts', 'skirt')
        possibilities['footwear'].append('casual shoes', 'running shoes', 'heels')
        possibilities['accessories'].append('cap')

    if f_rain == True :
        possibilities['tops'].append('rain coat')
        possibilities['accessories'].append('umbrella')
    
    if f_snow == True :
        possibilities['tops'].append('winter coat')

    return possibilities


if __name__ == "__main__" :

    ### Forecast ###
    today = str(date.today())
    c_raw_temp = mt.get_daily_forecast_raw_temp('c', 'max', today)
    f_rain = mt.will_it_rain(today)
    f_snow = mt.will_it_snow(today)