'''寻找第n个默尼森数。
代码格式如下：
def prime(num):
    ...
def monisen(no):
    … …
    return  xxx

print(monisen(int(input())))    #此处不需要自己输入，只要写这样一条语句即可，主要完成monisen()函数（4分）
经典程序设计问题：找第n个默尼森数。P是素数且M也是素数，并且满足等式M=2**P-1，则称M为默尼森数。
例如，P=5，M=2**P-1=31，5和31都是素数，因此31是默尼森数。
输入格式:按提示用input()函数输入
输出格式：int类型
输入样例：4
输出样例：127

时间限制：500ms内存限制：32000kb'''

def prime(num):
    if num < 1:
        return 0
    i = 2
    while i*i <= num:
        if num % i == 0:
            return 0
        i += 1
    return 1

def monisen(no):
    counter_monisen = 0
    num = 1
    while counter_monisen != no:
        num += 1
        is_prime = prime(num)
        if is_prime == 1:
            # print("num", num)
            unchecked_monisen_num = pow(2, num) - 1
            # print("uncheck_num", unchecked_monisen_num)
            unchecked_monisen_num = int(unchecked_monisen_num)
            check_num = prime(unchecked_monisen_num)
            # print("check_num", check_num)
            if check_num == 1:
                if counter_monisen+1 == no:
                    return unchecked_monisen_num
                counter_monisen += 1
print(monisen(int(input())))