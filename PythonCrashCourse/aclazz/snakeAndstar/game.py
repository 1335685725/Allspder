import random

words = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890./?\"\:()")

def word(words):
    return random.choice(words)


def start():
    score = 0
    while True:
        a = word(words)
        answer = input("请输入"+a+"\n").upper()
        if answer == a:
            score += 1
            print("输入正确，加一分， 现在分数为", score)
        else:
            print("输入错误")

if __name__ == '__main__':
    print("打字游戏")
    s = input("输入1开始游戏\n")
    if "1" == s:
        start()