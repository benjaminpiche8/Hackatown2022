import meteo as mt
from datetime import date
import random


def short_term_recommandation_top(sex = 'm') :
    c_raw_temp = mt.get_current_raw_temp('c')
    c_precip = mt.get_current_precip()

    possibilities_men = []
    possibilities_women = []

    if c_raw_temp < -5 :
        possibilities_men.append('long sleeves', 'hoodie', 'winter coat')
        possibilities_women.append('long sleeves', 'hoodie', 'light coat')

    if -5 <= c_raw_temp < 15 :
        possibilities_men.append('long sleeves', 'hoodie', 'light coat')
        possibilities_women.append('long sleeves', 'hoodie', 'light coat')

    if c_raw_temp >= 15 and sex == 'm':
        possibilities_men.append('t-shirt')

    if c_raw_temp >= 15 and sex == 'w':
        possibilities_women.append('t-shirt', 'dress')

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
        possibilities_women.append('pants', 'leggings')
    
    if c_raw_temp >= 15 and sex == 'w' :
        possibilities_women.append('shorts', 'skirt')

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
        possibilities_men.append('casual shoes', 'running shoes')
    
    if c_raw_temp >= 15 and sex == 'w' :
        possibilities_women.append('casual shoes', 'running shoes', 'heels')

    if sex == 'm' :
        return random.choice(possibilities_men)
    else :
        return random.choice(possibilities_women)


def short_term_recommandation_accessory() :
    c_raw_temp = mt.get_current_raw_temp('c')
    c_precip = mt.get_current_precip()

    possibilities = []

    if c_raw_temp < 0 :
        possibilities.append('hat', 'scarf', 'gloves')
    if c_raw_temp >= 0 :
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