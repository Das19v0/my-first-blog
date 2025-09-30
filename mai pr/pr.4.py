# name = input("Ведите ваше имя")
# print(name)
# age= input(name, " Сколько тебе лет?")
# print(age)
from django.template.defaultfilters import upper
from pyexpat.errors import messages

# number1= input("Ведите первое число ")
# print("Вы вели -", number1)
# number2 = input("Ведите второе число ")
# print("Вы вели второе число-", number2)
#
# print("Сумма этих чисел=", float(number1)+float(number2))
# print("Деление этих чисел=", float(number1)/float(number2))
# print("Умножение этих чисел=", float(number1)* float(number2))
# print("Вычитание этих чисел=", float(number1)- float(number2))
#
# message = "Hello Dasha!"
# print(message)
# name ="Maria"
# print(name)
#
# text=("Добро пожаловать в Python, "
#         "Python научит вас программированию")
# print(text)
# text = "Message: \"Hello World\""
# print(text)
# userName=input("Введите ваше имя- ")
# print(userName)
# userAge= input(f"Скoлько вам лет? {userName}")
# print(userAge)
# user= f"name: {userName} age: {userAge}"
# print(user)
# userId ="adc" # тип str
# print(userId)
#
# userId=234 # тип int
# print(userId)
# userId="adc"# тип str
# print(type(userId))# <class 'str'>
#
# userId = 234# тип int
# print(type(userId))# <class 'int'>
#
# name = input("Введите ваше имя: ")
# print(f"Ваше имя: {name}")
# age = input("Сколько вам лет?: ")
# print(f"Вам: {age}")
# print(f"Вас зовут: {name}, Вам {age}")
#
# name= input("Your name: ")
# age = input("Your age: ")
# print(f"Name: {name} Age: {age}")
# number = 5+6-9*30+9
# print(number)
# number1= (5+6)-(9*30+9)
# print(number1)
p= float(input("Начальная сумма вклада: "))
r= float(input("Процент по вкладу: "))
t= float(input("Количество лет: "))
si =(p*r*t)/100
print("Начисленные проценты: ", si)
