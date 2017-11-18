v = int(input('Введите число от 1 до 10: '))
a = v + 10
print(a)

name = input('Введите ваше имя: ')
print('Привет, ' + name + '. Как дела?')

mylist.append("Маша") # Добавляет элемент Маша в конец списка
mylist[2:4] # вернет элементы 2 и 3. 4 не вернет
mylist[-1] # берем последний элемент со списка
mylist.index("Петя") # ищем номер элемента Петя
mylist.sort() # сортируем список
'Вася' in mylist # Есть ли Вася в списке?
del mylist[3] # удалить элемент с 3 индексом
mylist.remove('Маша') # удалить первый попавшийся элемент Маша

mylist = [2, 3, 4, 5, 6, 7]
print(mylist)
mylist.append("Python")
print(mylist[0], mylist[5])
print(mylist[1:4])
len(mylist)
mylist.index(6)
mylist.remove("Python")

{"ключ": "значение"} # {'name': 'Маша', 'age': 25}
user["age"] = 25
user.get('name') # использовать get, чтоб программа не упала, если элемента нет
print(user.get())
del user["age"] # удаляем по ключу
user["friends"] = mylist
all_users = [
	{'name': 'Маша', 'age': 25}
	{'name': 'Паша', 'age': 21}
] # словарь со списками внутри

weather = {'city': 'Moscow', 'temperature': '20', 'wind': 'восточный'}
weather["city"]
weather["temperature"] = 31
print(weather["temperature"])
len(weather)
weather.get('country')
print(weather.get())
weather["date"] = '27.05.2017'
date_weather = []
d1 = {'date': '12.12.2016', 'temperature': '3'}
d2 = {'date': '13.12.2016', 'temperature': '2'}
d3 = {'date': '14.12.2016', 'temperature': '-1'}
date_weather.append(d1)
date_weather.append(d2)
date_weather.append(d3)
print(date_weather)

one = "How "
two = "are "
three = "you?"
def get_summ(one, two, three):
	resoult = one.upper() + two.upper() + three.upper()
	return print(resoult)
get_summ(one, two, three)

answer = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
question = input()
question = question.lower()
if question in answer.keys():
	def get_answer(question, answer): 
		return answer.get(question)
else:
	 exit()
print(get_answer(question, answer))