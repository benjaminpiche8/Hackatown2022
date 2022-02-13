import meteo as mt
from datetime import date
import random

def get_clothing_icon(item) : # string parameter with a clothing item
    return 'icons_clothes/' + str(item)

def short_term_recommandation_top(sex = 'm') :
    c_raw_temp = mt.get_current_raw_temp('c')
    c_precip = mt.get_current_precip()

    possibilities_men = []
    possibilities_women = []

    if c_raw_temp < -5 :
        items_men = ['long sleeves', 'hoodie', 'winter coat']
        items_women = ['long sleeves', 'hoodie', 'light coat']
        for item in items_men :
            possibilities_men.append(item)
        for item in items_women :
            possibilities_women.append(item)

    if -5 <= c_raw_temp < 15 :
        items_men = ['long sleeves', 'hoodie', 'light coat']
        items_women = ['long sleeves', 'hoodie', 'light coat']
        for item in items_men :
            possibilities_men.append(item)
        for item in items_women :
            possibilities_women.append(item)

    if c_raw_temp >= 15 and sex == 'm':
        possibilities_men.append('t-shirt')

    if c_raw_temp >= 15 and sex == 'w':
        items_women = ['t-shirt', 'dress']
        for item in items_women :
            possibilities_women.append(item)

    if c_precip > 0 :
        possibilities_men.append('rain coat')
        possibilities_women.append('rain coat')

    if sex == 'm' :
        return random.choice(possibilities_men)
    else :
        return random.choice(possibilities_women)


def short_term_recommandation_bottom(sex = 'm') :
    c_raw_temp = mt.get_current_raw_temp('c')

    possibilities_men = []
    possibilities_women = []

    if c_raw_temp < 15 and sex == 'm' :
        possibilities_men.append('pants')

    if c_raw_temp >= 15 and sex == 'm' :
        possibilities_men.append('shorts')

    if c_raw_temp < 15 and sex == 'w' :
        items_women = ['pants', 'leggings']
        for item in items_women :
            possibilities_women.append(item)

    if c_raw_temp >= 15 and sex == 'w' :
        items_women = ['shorts', 'skirt']
        for item in items_women :
            possibilities_women.append(item)

    if sex == 'm' :
        return random.choice(possibilities_men)
    else :
        return random.choice(possibilities_women)


def short_term_recommandation_footwear(sex = 'm') :
    c_raw_temp = mt.get_current_raw_temp('c')

    possibilities_men = []
    possibilities_women = []

    if c_raw_temp < -5 :
        possibilities_men.append('boots')
        possibilities_women.append('boots')

    if (-5 <= c_raw_temp < 15) :
        possibilities_men.append('casual shoes')
        possibilities_women.append('casual shoes')

    if c_raw_temp >= 15 and sex == 'm' :
        items_men = ['casual shoes', 'running shoes']
        for item in items_men :
            possibilities_men.append(item)        
    
    if c_raw_temp >= 15 and sex == 'w' :
        items_women = ['casual shoes', 'running shoes', 'heels']
        for item in items_women :
            possibilities_women.append(item)

    if sex == 'm' :
        return random.choice(possibilities_men)
    else :
        return random.choice(possibilities_women)


def short_term_recommandation_accessory() :
    c_raw_temp = mt.get_current_raw_temp('c')
    c_precip = mt.get_current_precip()

    possibilities = []

    if c_raw_temp < 0 :
        items = ['hat', 'scarf', 'gloves']
        for item in items :
            possibilities.append(item)

    else :
        possibilities.append('cap')

    if c_precip == True :
        possibilities.append('umbrella')

    return random.choice(possibilities)


if __name__ == "__main__" :

    ### Forecast ###
    today = str(date.today())
    c_raw_temp = mt.get_daily_forecast_raw_temp('c', 'max', today)
    f_rain = mt.will_it_rain(today)
    f_snow = mt.will_it_snow(today)