#4.4.1
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
#4.4.2
for player in players[:3]:
    print(player)
#4.4.3
myfood = ['pizza', 'falafei', 'carrot cat']
friend_food = myfood[:]
print(myfood)
print(friend_food)
myfood.append("cannoli")
friend_food.append("ice cream")
print(myfood)
print(friend_food)
friend_food = myfood
myfood.append("cannoli1")
friend_food.append("ice")
print(myfood)
print(friend_food)
#Ex4-10
myfood = ['pizza', 'falafei', 'carrot cat', 'ice cream']
print(myfood[:3])
print(myfood[1:4])
print(myfood[-3:])
#4-11
pizzas = ["abc", "asd", "qwe"]
friend_pizzas = pizzas[:]
pizzas.append("aaa")
friend_pizzas.append("sss")
print("my pizzas")
for i in pizzas:
    print(i)
print("my friend pizzas")
for i in friend_pizzas:
    print(i)
#4-12
for food in myfood:
    print(food)
for food in friend_food:
    print(food)



