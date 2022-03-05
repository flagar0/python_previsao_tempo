import requests
import json


class Tempo:
    def __init__(self,city):
        self.existe = True
        request = requests.get("https://api.hgbrasil.com/weather?woeid="+city+"?key=9ef3cde2")
        dados = json.loads(request.content)
        self.data = dados['results']
        self.cidade = city
        

def gera_img(code, hora):
    code = int(code)
    if(code >=0 and code <= 4):
        return "https://www.gstatic.com/images/icons/material/apps/weather/2x/strong_tstorms_dark_color_96dp.png"

    elif(code >=5 and code <= 8):
        return "https://www.gstatic.com/images/icons/material/apps/weather/2x/wintry_mix_rain_snow_dark_color_96dp.png"

    elif(code >=9 and code <=12):
        return "https://www.gstatic.com/images/icons/material/apps/weather/2x/drizzle_dark_color_96dp.png"

    elif(code >=13 and code <= 16):
        return "https://www.gstatic.com/images/icons/material/apps/weather/2x/flurries_dark_color_96dp.png"

    elif(code >=17 and code <= 22):
        return "https://www.gstatic.com/images/icons/material/apps/weather/2x/blizzard_dark_color_96dp.png"

    elif(code >=23 and code <= 24):
        return "https://www.gstatic.com/images/icons/material/apps/weather/2x/blizzard_dark_color_96dp.png"

    elif((code >=25 and code <= 26 )or code==28):
        if(hora=="dia"):
            return "https://www.gstatic.com/images/icons/material/apps/weather/2x/mostly_cloudy_day_dark_color_96dp.png"
        else:
            return "https://www.gstatic.com/images/icons/material/apps/weather/2x/mostly_cloudy_night_dark_color_96dp.png"

    elif(code ==27 or code == 31 or code == 33 or code == 32):
        if(hora=="dia"):
            return "https://www.gstatic.com/images/icons/material/apps/weather/2x/sunny_dark_color_96dp.png"
        else:
            return "https://www.gstatic.com/images/icons/material/apps/weather/2x/clear_night_dark_color_96dp.png"
    
    elif(code ==29 or code == 30):
        if(hora=="dia"):
            return "https://www.gstatic.com/images/icons/material/apps/weather/2x/partly_cloudy_dark_color_96dp.png"
        else:
            return "https://www.gstatic.com/images/icons/material/apps/weather/2x/partly_cloudy_night_dark_color_96dp.png"

    elif(code ==34):
        return "https://www.gstatic.com/images/icons/material/apps/weather/2x/mostly_sunny_dark_color_96dp.png"
    
    elif(code ==35):
        return "https://www.gstatic.com/images/icons/material/apps/weather/2x/showers_rain_dark_color_96dp.png"    
            
    elif(code ==36):
        return "https://www.gstatic.com/images/icons/material/apps/weather/2x/sunny_dark_color_96dp.png"  
            
    elif(code >=37 and  code <=39):
        if(hora=="dia"):
            return "https://www.gstatic.com/images/icons/material/apps/weather/2x/isolated_scattered_tstorms_day_dark_color_96dp.png"
        else:
            return "https://www.gstatic.com/images/icons/material/apps/weather/2x/isolated_scattered_tstorms_night_dark_color_96dp.png" 
            
    elif((code >=40 and  code <=43) or (code >=46 and  code <=47)):
        if(hora=="dia"):
            return "https://www.gstatic.com/images/icons/material/apps/weather/2x/scattered_showers_day_dark_color_96dp.png"
        else:
            return "https://www.gstatic.com/images/icons/material/apps/weather/2x/scattered_showers_night_dark_color_96dp.png"   

    elif(code ==44):
        return "https://www.gstatic.com/images/icons/material/apps/weather/2x/mostly_sunny_dark_color_96dp.png"  
            
    elif(code ==45):
        return "https://www.gstatic.com/images/icons/material/apps/weather/2x/heavy_rain_dark_color_96dp.png"  
            
    elif(code ==48):
        if(hora=="dia"):
            return "https://www.gstatic.com/images/icons/material/apps/weather/2x/sunny_dark_color_96dp.png"
        else:
            return "https://www.gstatic.com/images/icons/material/apps/weather/2x/clear_night_dark_color_96dp.png"

        