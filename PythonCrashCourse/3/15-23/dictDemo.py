#6 字典
alien = {"color":"green", "points":5}
print(alien["color"])
print(alien["points"])
alien["x_position"] = 0
alien["color"] = "yellow"
del alien["points"]
print("My favorite color is" + alien["color"].title() +".")
#Ex6-1
My_friend = {
    "first_name" : "feng",
    "last_name" : "an",
    "age" : 20,
    "city" : "nanjing"
}
for k, v in My_friend.items():
    print(k + ":" + str(v))
#Ex6-2
a_dic = {"aaa": 1,
         "bbb": 2,
         "ccc": 3,
         "ddd": 4,
         "eee": 5
}
for k, v in a_dic.items():
    print(k +":"+ str(v))
#6.3.2
for k in a_dic.keys():
    print(k)
#6.3.3
for k in sorted(a_dic.keys()):
    print(k)
#6.3.4
for v in a_dic.values():
    print(k)
# 6.4.1嵌套
alien0 = {"color":"green", "points":5}
alien1 = {"color":"yellow", "points":10}
alien2 = {"color":"green", "points":15}
aliens = [alien0, alien1, alien2]
for alien in aliens:
    print(alien)
#字典中存储列表啊
dict0 = {
    "crust": "thick",
    "topping": ["mushroom", "extra cheese"]
}
for top in dict0["topping"]:
    print(top)

favorite_languages = {
    "jen": ["python", "ruby"],
    "sarsh": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"]
}
for name, languages in favorite_languages.items():
    for language in languages:
        print(name + "\t" + language)

#6.4.3在字典中存储字典
users = {
    "favorite_languages": {
        "jen": ["python", "ruby"],
        "sarsh": ["c"],
        "edward": ["ruby", "go"],
        "phil": ["python", "haskell"]
    },
    "My_friend": {
        "first_name": "feng",
        "last_name": "an",
        "age": 20,
        "city": "nanjing"
    }
}
for user_name, user_word in users.items():
    for k, v in user_word.items():
        print(user_name + "\t" + k + "\t" + v)























