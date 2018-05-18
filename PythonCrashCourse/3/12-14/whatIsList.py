#3.1
bicycle = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycle)
#3.11
print(bicycle[0])
print(bicycle[0].title())
#3.1.2
print(bicycle[1])
print(bicycle[3])
#3.1.3
message = "My first bicycle was a "+ bicycle[0].title() +"."
print(message)
#Ex3-1
names = ["123","456","asd"]
for name in names:
    print(name)
# Ex3-2
for name in names:
    print(name,"Hello")
#Ex3-3
ways = ["bike", "car", "walk",'']
print("I would like to own a " + ways[0] + ".")
print("I would like to own a " + ways[1] + ".")
print("I would like to own a " + ways[2] + ".")
#3.2.1
names[0] = "asdd"
#3.2.2
names.append("asgg")
print(names)
names.insert(0,"duuu")
print(names)
#3.2.3
del names[0]
print(names)
name = names.pop()
print(name)
print(names)
a_name = names.pop(1)
print(a_name)
names.remove("duuu")
print(names)
# Ex3-5
guest = ["123",'456',"789"]
print(guest[0],"无法赴约")
guest[0] = "321"
for a_guest in guest:
    print(a_guest,"快来")
#Ex3-6
print("I find a bigger desk")
guest.insert(0,"147")
guest.insert(int(len(guest)),"258")
guest.append(333)
# Ex3-7
while len(guest) > 2:
    aaa =  guest.pop()
    print(aaa,"yon can not")
for a_guest in guest:
    print(a_guest,"you can")
del guest[0]
del guest[0]
print(guest == [])
