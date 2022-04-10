import os
import json
import datetime
import requests
import pprint as pp

from dotenv import load_dotenv
load_dotenv()

class WeatherClient:
    OPEN_WEATHER_MAP_API = os.environ.get('OPEN_WEATHER_MAP_API')
    DEFAULT_ZIP_CODE = '77056'
    DEFAULT_LAT = 29.76
    DEFAULT_LONG = 95.36

    @classmethod
    def get_seven_day_forecast(cls, lat_long=None):
        if not lat_long:
            lat_long = (cls.DEFAULT_LAT,cls.DEFAULT_LONG)

        try:
            # https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={API key}

            URL = f'https://api.openweathermap.org/data/2.5/onecall?units=imperial&lat={lat_long[0]}&lon={lat_long[1]}&exclude=[current,minutely,hourly,alerts]&appid={cls.OPEN_WEATHER_MAP_API}'
            print(URL)
            r = requests.get(URL)

            pp.pprint(r.json())
            
            return r.json()
        except requests.exceptions.RequestException as e:
            print('Unable to get 7 day forecast')
            print(str(e))
            raise e

    @classmethod
    def get_seven_forecast_formatted(cls, lat_long=None) -> str:
        if not lat_long:
            lat_long = (cls.DEFAULT_LAT,cls.DEFAULT_LONG)

        forecasts = cls.get_seven_day_forecast(lat_long)
        lat_long = str(forecasts['lat'])+"_"+str(forecasts['lon'])
        formatted_forecasts = []

        # track 24 hour forecast each day
        for i in range(0, len(forecasts['daily'])):
            forecast = forecasts['daily'][i]
            # print(forecast)

            try:
                forecast_datetime = datetime.datetime.fromtimestamp(forecast['dt'])
                # forecast['dt_formatted'] = f'{forecast_datetime:%a, %b %d %-I:%M %p}'
                forecast['dt_formatted'] = f'{forecast_datetime:%d-%m-%Y}'
                
                forecast['weather_description'] = forecast['weather'][0]['description']
                forecast['weather_icon'] = cls.get_icon_url(forecast['weather'][0]['icon'])

                del forecast['dt']
                del forecast['feels_like']
                del forecast['weather']
                # del forecast['temp']

                formatted_forecasts.append(forecast)
            except KeyError as e:
                print(str(e))
                print('Unable to parse keys, skipping forecast')
            except Exception as e:
                print(str(e))
                print('Unable to format, skipping forecast')
        pp.pprint(json.dumps({'lat_long': lat_long, 'forecasts': formatted_forecasts}))
        return json.dumps({'lat_long': lat_long, 'forecasts': formatted_forecasts})

    @classmethod
    def get_icon_url(cls, icon):
        return f'https://openweathermap.org/img/wn/{icon}@2x.png'
