import pyowm
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here
owm = pyowm.OWM('594549d1efa72beefda55cc2acbe9428', config_dict)
mgr = owm.weather_manager()
place=input('Введите город: ')
observation = mgr.weather_at_place(place)
w = observation.weather.detailed_status
temp_dict_celsius = observation.weather.temperature('celsius')['temp']
wind_dict_in_meters_per_sec = observation.weather.wind()['speed']
print ('В городе '+ place+' сейчас '+ w +', температура ' + str(round(temp_dict_celsius))+' градусов по Цельсию, ветер '+str(wind_dict_in_meters_per_sec) + ' м/c.')
if temp_dict_celsius<10:
    print('Одевай тёплую ветровку и брюки!')
elif temp_dict_celsius>=10 and temp_dict_celsius <=20:
    print('Одевай лёгкую ветровку и лёгкие штаны!')
elif temp_dict_celsius>20:
    print('Одевай футболку и лёгкие брюки или шорты: на улице тепло!')
print('Нажми любую кнопку, чтобы завершить работы программы!')
input()