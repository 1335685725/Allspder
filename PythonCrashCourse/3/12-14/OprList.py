
#4.1遍历列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
#4.1.2
for magician in magicians:
    print(magician.title(), + ", that was a great trick")
    print("\nI can't wait to see your next trick , ",magician )
#4.1.3
for magician in magicians:
    print(magician.title(), + ", that was a great trick")
    print("\nI can't wait to see your next trick , ",magician )
print("Thank you, everyone. That was a great magic show")
#Ex4-1 比萨
pizzas = ["abc", "asd", "qwe"]
for pizza in pizzas:
    print("I like ", pizza ," pizza")
print("I like ",pizzas[0],pizzas[1],pizzas[2])
print("I really love pizza")
#Ex4-2
animals = ['cat', 'dog', 'pig']
for animal in animals:
    print(animal)
for animal in animals:
    print("A " + animal + "would make a great pet")
print("Any of those animals would make a great pet")
#4-3创建数值列表
for value in range(1,5):
    print(value)
#4.3.2
numbers = list(range(1,5))
print(numbers)
even_numbers = list(range(2,11,2))
print(even_numbers)
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    print(squares)
squares = []
for value in range(1,11):
    squares.append(value**2)
    print(squares)
#4.3.3
digit = list(range(1,11))
print(min(digit))
print(max(digit))
print(sum(digit))
# 4.3.4
squares = [value**2 for value in  range(1,11)]
print(squares)
# Ex4-3
for i in range(1,21):
    print(i)
#Ex4-4
a_list = [i for i in range(1,1000000)]
print(max(a_list))
print(min(a_list))
#Ex4-5
import time
start = time.clock()
print(sum(a_list))
end = time.clock()
print(start - end)
#Ex4-6
a_list = [i for i in range(1,21,2)]
for i in a_list:
    print(i)
# Ex4-7
a_list = [i for i in range(3,31) if i % 3 ==0]
print(a_list)
#Ex4-8
#Ex4-9
a_list = [i**3 for i in range(1,11)]
print(a_list)

