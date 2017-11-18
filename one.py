a = {'city': 'Moscow', 'temperature': '20', 'wind': 'восточный'}
b = {'city': 'St. Pt', 'temperature': '18', 'wind': 'северный'}
c = {'city': 'Sochy', 'temperature': '35', 'wind': 'южный'}
# weather = {'Ann': a, 'Bill': b, 'Carl': c}
# while True:	
	# question = input('Введите Ваше имя: ')
	# if question in weather.keys():
	# 	print(weather[question])
	# else:
	# 	print('Данного имени нет в базе, повторите попытку.')




plan = ['Ann', 'Benn', 'Coll']
question = input('Введите Ваше имя: ')
if question in plan.index():
	print("Ok")