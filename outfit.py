import meteo as mt
from datetime import date


def create_wardrobe() :
    wardrobe = {
        'tops' : [],
        'bottoms' : [],
        'footwear' : [],
        'accessories' : []
    }

    return wardrobe


def short_term_recommandations(sex) :
    recommandations = create_wardrobe()
    c_raw_temp = mt.get_current_raw_temp('c')
    c_feelslike_temp = mt.get_current_feelslike_temp('c')
    c_precip = mt.get_current_precip()

    if (c_raw_temp <= -5 or c_feelslike_temp <= -10) and sex == 'm':
        recommandations['tops'].append('long sleeves', 'hoodie', 'winter coat')
        recommandations['bottoms'].append('pants')
        recommandations['footwear'].append('boots')
        recommandations['accessories'].append('hat', 'scarf', 'gloves')

    if (c_raw_temp <= -5 or c_feelslike_temp <= -10) and sex == 'w':
        recommandations['tops'].append('long sleeves', 'hoodie', 'winter coat')
        recommandations['bottoms'].append('pants', 'leggings')
        recommandations['footwear'].append('boots')
        recommandations['accessories'].append('hat', 'scarf', 'gloves')

    if ((-5 < c_raw_temp <= 15) or (-10 < c_feelslike_temp <= 20)) and sex == 'm':
        recommandations['tops'].append('long sleeves', 'hoodie', 'light coat')
        recommandations['bottoms'].append('pants')
        recommandations['footwear'].append('boots')
        recommandations['accessories'].append('hat', 'scarf', 'gloves')

    if ((-5 < c_raw_temp <= 15) or (-10 < c_feelslike_temp <= 20)) and sex == 'w':
        recommandations['tops'].append('long sleeves', 'hoodie', 'light coat')
        recommandations['bottoms'].append('pants', 'leggings')
        recommandations['footwear'].append('casual shoes')
        recommandations['accessories'].append('hat', 'cap')

    if (c_raw_temp > 15 or c_feelslike_temp > 20) and sex == 'm':
        recommandations['tops'].append('t-shirt')
        recommandations['bottoms'].append('shorts')
        recommandations['footwear'].append('casual shoes', 'running shoes')
        recommandations['accessories'].append('cap')

    if (c_raw_temp > 15 or c_feelslike_temp > 20) and sex == 'w':
        recommandations['tops'].append('t-shirt', 'dress')
        recommandations['bottoms'].append('shorts', 'skirt')
        recommandations['footwear'].append('casual shoes', 'running shoes', 'heels')
        recommandations['accessories'].append('cap')

    if c_precip > 0 :
        recommandations['tops'].append('rain coat')
        recommandations['accessories'].append('umbrella')

    return recommandations


def long_term_recommandations(f_raw_temp, f_rain, f_snow, sex) :
    recommandations = create_wardrobe()

    if f_raw_temp < -5 and sex == 'm' :
        recommandations['tops'].append('long sleeves', 'hoodie', 'winter coat')
        recommandations['bottoms'].append('pants')
        recommandations['footwear'].append('boots')
        recommandations['accessories'].append('hat', 'scarf', 'gloves')

    if (-5 <= f_raw_temp < 15) and sex == 'm' :
        recommandations['tops'].append('long sleeves', 'hoodie', 'light coat')
        recommandations['bottoms'].append('pants')
        recommandations['footwear'].append('boots')
        recommandations['accessories'].append('hat', 'scarf', 'gloves')

    if f_raw_temp > 15 and sex == 'm' :
        recommandations['tops'].append('t-shirt')
        recommandations['bottoms'].append('shorts')
        recommandations['footwear'].append('casual shoes', 'running shoes')
        recommandations['accessories'].append('cap')

    if f_raw_temp < -5 and sex == 'w' :
        recommandations['tops'].append('long sleeves', 'hoodie', 'winter coat')
        recommandations['bottoms'].append('pants', 'leggings')
        recommandations['footwear'].append('boots')
        recommandations['accessories'].append('hat', 'scarf', 'gloves')

    if (-5 <= f_raw_temp < 15) and sex == 'w' :
        recommandations['tops'].append('long sleeves', 'hoodie', 'light coat')
        recommandations['bottoms'].append('pants', 'leggings')
        recommandations['footwear'].append('casual shoes')
        recommandations['accessories'].append('hat', 'cap')
    
    if f_raw_temp > 15 and sex == 'w' :
        recommandations['tops'].append('t-shirt', 'dress')
        recommandations['bottoms'].append('shorts', 'skirt')
        recommandations['footwear'].append('casual shoes', 'running shoes', 'heels')
        recommandations['accessories'].append('cap')

    if f_rain == True :
        recommandations['tops'].append('rain coat')
        recommandations['accessories'].append('umbrella')
    
    if f_snow == True :
        recommandations['tops'].append('winter coat')

    return recommandations


if __name__ == "__main__" :

    today = str(date.today())

    ### Current ###
    # c_raw_temp = mt.get_current_raw_temp('c')
    # c_feelslike_temp = mt.get_current_feelslike_temp('c')
    # c_precip = mt.get_current_precip()

    ### Forecast ###
    c_raw_temp = mt.get_daily_forecast_raw_temp('c', 'max', today)
    f_rain = mt.will_it_rain(today)
    f_snow = mt.will_it_snow(today)