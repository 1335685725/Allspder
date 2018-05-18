

#7.1 input
name = input("your name:")
print(name)
age = int(input("age:"))
if age > 18:
    print("OK")
#7.2while
current_num = 1
while current_num <= 5:
    print("OK")
    current_num +=1
#7.2.2
msg = ""
while msg != "q":
    msg = input("message:")
    print(msg)
#7.3.1
unconfirmed_users = ["aaa", "bbb", "ccc"]
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
#7.3.2
while "bbb" in unconfirmed_users:
    unconfirmed_users.remove("bbb")
#7.3.3
responses = {}
polling_active = True
while polling_active:
    name = input("your name :")
    response = input("your answer :")
    responses[name] = response
    repeat = input("continue? yes/no")
    if repeat == "no":
        polling_active = False

for k, v in responses.items():
    print(k + v)

