import random
import time
from threading import Thread

words = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890./?\"\:()")
answer = None

def check(second):
    time.sleep(second)
    if answer != None:
        return
    print("too slow")
    return "slow"

def produce(words):
    return random.choice(words)


def start():
    score = 0
    second = 3.01
    while True:
        if second <= 1.20:
            second -=0.01
        a = produce(words)
        answer = input(f"请在{second}秒内输入{a}\n").upper()
        # 如何让线程里的函数反馈到主循环里。。。
        Thread(target=check(second)).start()
        if "~" == answer:
            print("退出游戏, 你的总分是：",score)
            exit(0)
        if answer == a:
            score += 1
            print("输入正确，加一分， 现在分数为", score)
        else:
            print("输入错误，不加分")

if __name__ == '__main__':
    print("打字游戏".center(20))
    s = input("提示:输入s开始游戏\n")
    print("提示:输入“~”结束游戏")
    if "s" == s:
        start()