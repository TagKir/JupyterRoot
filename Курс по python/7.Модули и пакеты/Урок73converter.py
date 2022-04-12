#Это Урок 73---Ещё раз о __name__ и __main__ -1часть
def to_inches(cm):
	return cm*0.393701

def to_miles(km):
	return km*0.621371

def to_fahrenheit(celsius):
	return (celsius*9/5)+32

if __name__=='__main__':#если скрипт будет выполнен напрямую,то name будет равен '__main__'
	print('call a converting func that you want')#Перевод:назовите функцию преобразования, которую вы хотите
else:#Если функция была импортированна
	print('was imported (not executed  directly)')#Перевод:был импортирован (не выполнялся напрямую)
#Если вызываю,выводит call a converting func that you want