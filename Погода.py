import pyowm

owm = pyowm.OWM('2582fe667f2be8e56bfd6363bfaa8046', language='ru')
place = input('Город: ')
observation = owm.weather_at_place(place)
w = observation.get_weather()
# wind = w.get_wind()             # {'speed': 4.6, 'deg': 330}
temp = w.get_temperature('celsius')['temp']
print('В городе ' + place + ' сейчас ' + w.get_detailed_status())
print('Температура: ' + str(temp))
# print('Ветер: ' + str(wind))['speed']

