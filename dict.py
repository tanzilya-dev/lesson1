dict_city = {"city": "Москва", "temperature": "20"}
print(dict_city['city'])
dict_city['temperature'] = str(int(dict_city['temperature']) - 5)
print(dict_city)

print(dict_city.get('country'))
print(dict_city.get('country', 'Россия'))
dict_city['date'] = '27.05.2019'
print(dict_city)
print(len(dict_city))