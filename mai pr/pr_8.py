# '''введи количество элементов в списке'''
# number=input("Введите число")
# text=input()
#
# numbers=[1,2,3,4,5]
# people=["Tom", "Sam", "Bob"]
#
# numbers1=[]
# numbers2=list()
#
# numbers=[1,2,3,4,5]
# people=["Tom", "Sam", "Bob"]
#
# print(numbers)
# print(people)
#
# numbers1=[1,2,3,4,5]
# numbers2 = list(numbers1)
# print(numbers2)
#
# letters=list("Hello")
# print(letters)
#
# numbers=[5]*6
# print(numbers)
#
# people=["Tom"]*3
# print(people)
#
# students=["Bob", "Sam"]*2
# print(students)
#
# people=["Tom", "Sam", "Bob"]
# print(people[0])
# print(people[1])
# print(people[2])
#
# print(people[-2])
# print(people[-1])
# print(people[-3])
#
# people=["Tom", "Sam", "Bob"]
#
# people[1]="Mike"
# print(people[1])
# print(people)
#
# people=["Tom","Bob", "Sam"]
# tom, bob, sam=people
# print(tom)
# print(bob)
# print(sam)
#
# people=["Tom", "Sam", "Bob"]
# for person in people:
#     print(person)
#
# people=["Tom", "Sam", "Bob"]
# i=0
# while i <len(people):
#     print(people[i])
#     i+=1
#
# numbers1=[1,2,3,4,5]
# numbers2=list([1,2,3,4,5])
# if numbers1 ==numbers2:
#     print("numbers1 equal to numbers2")
# else:
#     print("numbers1 is not equal to numbers2")
#
# people=["Tom","Bob", "Alice", "Tim", "Bill"]
# slice_people1=people[:3]
# print(slice_people1)
#
# slice_people2=people[1:3]
# print(slice_people2)
#
# slice_people3=people[1:6:2]
# print(slice_people3)
#
# people=["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
# slice_people1=people[:-1]
# print(slice_people1)
#
# slice_people2=people[-3:-1]
# print(slice_people2)
#
from dis import disco
from operator import index
from tkinter.font import names

from django.contrib.auth import aget_user
from django.db.models.expressions import result

#
# people = ["Tom", "Bob"]
#
# # добавляем в конец списка
# people.append("Alice")  # ["Tom", "Bob", "Alice"]
# # добавляем на вторую позицию
# people.insert(1, "Bill")  # ["Tom", "Bill", "Bob", "Alice"]
# # добавляем набор элементов ["Mike", "Sam"]
# people.extend(["Mike", "Sam"])  # ["Tom", "Bill", "Bob", "Alice", "Mike", "Sam"]
# # получаем индекс элемента
# index_of_tom = people.index("Tom")
# # удаляем по этому индексу
# removed_item = people.pop(index_of_tom)  # ["Bill", "Bob", "Alice", "Mike", "Sam"]
# # удаляем последний элемент
# last_item = people.pop()  # ["Bill", "Bob", "Alice", "Mike"]
# # удаляем элемент "Alice"
# people.remove("Alice")  # ["Bill", "Bob", "Mike"]
# print(people)  # ["Bill", "Bob", "Mike"]
# # удаляем все элементы
# people.clear()
# print(people)  # []
#
# people=["Tom", "Bob", "Alice", "Sam"]
# if "Alice" in people:
#     people.remove("Alice")
# print(people)
#
# people=["Tom", "Bob", "Alice", "Sam", "Bill", "Kate", "Mike"]
# del people[1]
# print(people)
# del people[:3]
# print(people)
# del people[1:]
# print(people)
#
# nums=[10,20,30,40,50]
# nums[1:4]=[11,22]
# print(nums)
#
# people=["Tom", "Bob", "Alice", "Tom", "Bill", "Tom"]
#
# people_count=people.count("Tom")
# print(people_count)
#
# people=["Tom", "Bob", "Alice", "Sam", "Bill"]
# people.sort()
# print(people)
#
# people=["Tom", "Bob", "Alice", "Sam", "Bill"]
# people.sort()
# people.reverse()
# print(people)
#
# people=["Tom", "Bob", "Alice", "Sam", "Bill"]
#
# people.sort()
# print(people)
#
# people.sort(key=str.lower)
# print(people)
#
# people=["Tom", "Bob", "Alice", "Sam", "Bill"]
# sorted_people=sorted(people, key=str.lower)
# print(sorted_people)
#
# numbers=[-5, -4, -3 ,-2, -1, 0, 1, 2, 3, 4, 5]
# def condition(number): return number>1
# result=filter(condition,numbers)
# for n in result: print(n, end= " ")
#
# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
# people=[Person ("Tom", 38), Person("Kate", 31), Person("Bob",42),
#         Person("Alice",34), Person("Sam", 25)]
# view=filter(lambda p:p.age>33, people)
# for person in view:
#     print(f"Name:{person.name} Age: {person.age}")
#
# numbers=[1,2,3,4,5]
# def square(number): return number * number
# result=map(square, numbers)
# for n in result: print(n, end=" ")
#
# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
# people=[ Person("Tom", 38), Person("Kate", 31), Person("Bob", 42),
#         Person("Alice", 34),  Person("Sam", 25) ]
# view=map(lambda p:p.name, people)
# for person in view:
#     print(person)
#
# numbers=[9,21,12,1,3,15,18]
# print(min(numbers))
# print(max(numbers))
#
# people1=["Tom", "Bob", "Alice"]
# people2=people1.copy()
# people2.append("Sam")
# print(people1)
# print(people2)
#
# people1=["Tom", "Bob", "Alice"]
# people2=["Tom", "Sam", "Tim", "Bill"]
# people3=people1+people2
# print(people3)
#
# people=[
#     ["Tom", 29],
#     ["Alice", 33],
#     ["Bob", 27]
# ]
# print(people[0])
# print(people[0][0])
# print(people[0][1])
#
# people = [
#     ["Tom", 29],
#     ["Alice", 33],
#     ["Bob", 27]
# ]
# person=list()
# person.append("Bill")
# person.append(41)
# people.append(person)
# print(people[-1])
# people[-1].append("+79876543210")
# print(people[-1])
# people[-1].pop()
# print(people[-1])
# people.pop(-1)
# people[0]=["Sam", 18]
# print(people)
#
# people=[
#     ["Tom", 29],
#     ["Alice", 33],
#     ["Bob", 27]
# ]
# for person in people:
#     for item in person:
#         print(item, end="|")
#
# fact=lambda n:[1,0] [n>1] or fact (n-1)*n
# print(fact(4))
#
names = ["Tom", "Bob", "Sam"]
names.append("Alice")
names.append("Kate")
names.pop()
print(names)