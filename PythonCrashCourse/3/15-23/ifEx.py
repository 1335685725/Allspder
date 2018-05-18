#5.1
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#5.2.4
answer = 18
if answer !=42:
    print("That is nuo the correct answer. Please try again!")
#5.2.5
if answer != 42 and answer != 50:
    print("buxinagdeng")
#5.2.6
if 'audi' in cars:
    print("in")
#5.2.7
if 'www' not in cars:
    print("not in")
#Ex5-1
car = "subaru"
print(car == 'audi')
print(car == 'subaru')
#5.3.3
age = 12
if age < 4:
    print('$0')
elif age < 18:
    print("$5")
else:
    print("$10")
#5-3 外星人颜色#1

alien_color='green'
if alien_color=='green':
    print('This player got 5 points!')
alien_color='red'
if alien_color=='green':
    print('This player got 5 points!')
#2
alien_color='green'
if alien_color=='green':
    print('This player got 5 points!')
else:
    print('This player got 10 points!')
alien_color='yellow'
if alien_color=='green':
    print('This player got 5 points!')
else:
    print('This player got 10 points!')
#3
alien_color='green'
if alien_color=='green':
    print('This player got 5 points!')
elif alien_color=='yellow':
    print('This player got 10 points!')
else:
    print('This player got 15 points!')
alien_color='yellow'

if alien_color=='green':
    print('This player got 5 points!')
elif alien_color=='yellow':
    print('This player got 10 points!')
else:
    print('This player got 15 points!')
alien_color='green'
if alien_color=='red':
    print('This player got 5 points!')
elif alien_color=='yellow':
    print('This player got 10 points!')
else:
    print('This player got 15 points!')
age=32
if age<2:
    print('He is a baby!')
elif age>=2 and age<4:
    print('He is toddling!')
elif age>=4 and age<13:
    print('He is a child!')
elif age>=13 and age<20:
    print('He is a teenager!')
elif age>=20 and age<65:
    print('He is an adult!')
else:
    print('He is an aged man!')
favorite_fruits=['orange','cherry','watermelon']
if 'orange' in favorite_fruits:
    print("You really like orange!")
if 'cherry' in favorite_fruits:
    print("You really like cherry!")
if 'apple' in favorite_fruits:
    print("You really like apple!")
if 'pear' in favorite_fruits:
    print("You really like pear!")
if 'watermelon' in favorite_fruits:
    print("You really like watermelon!")
#5.4
#5-8
users=['admin','bing','yang','ling','fei']
for user in users:
    if user=='admin':
        print('Hello admin,would you like to see a status report?')
    else:
        print('Hello '+user.title()+",thank you for logging in again!")
users=[]
if  users:
    for user in users:
        if user=='admin':
            print('Hello admin,would you like to see a status report?')
        else:
            print('Hello '+user.title()+",thank you for logging in again!")
else:
    print('We need to find some users!')
current_users=['admin','bing','yang','ling','fei']
new_users=['wang','Bing','Yang','wen','ma']
for new_user in new_users:
        if new_user.lower()  not in current_users:
            print(new_user.lower()+',This user is available!')
        else:
            print(new_user.lower()+',This user is forbidden!')
sequences=list(range(1,10))
for sequence in sequences:
    if sequence<=3 :
        if sequence==1 :
            print('1st')
        if sequence==2 :
            print('2nd')
        if sequence==3 :
            print('3rd')
    else:
        print(str(sequence)+'th')










