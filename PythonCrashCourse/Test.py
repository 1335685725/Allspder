# Test
import time
# import re
#
# List = ["   123,654,789,120","123.4.231.333    ", "\n123,654,654,321   "]
# RRList = []
# for i in List:
#     RRList.append((re.sub('\n', '', str(i))).strip())
# print(RRList)
# start = time.clock()
# a_list = [i for i in range(3, 30) if i % 3 == 0]
# print(a_list)
# # a_list = [3, 6, 9, 12, 15, 18, 21, 24, 27]
# a_list.extend([a_list.pop(), a_list.pop()])
# print(a_list)
# print(a_list.__str__())
# end = time.clock()
# print(end - start)
#
# # reverse -1 and -2
# start = time.clock()
# a_list = [i for i in range(3, 30, 3)]
# print(a_list)
# # a_list = [3, 6, 9, 12, 15, 18, 21, 24, 27]
# a_list.extend([a_list.pop(), a_list.pop()])
# print(a_list)
# print(a_list.__str__())
# end = time.clock()
# print(end - start)



def prime(num):
    if num < 1:
        return 0
    i = 2
    while i*i <= num:
        if num % i == 0:
            return 0
        i += 1
    return 1

for i in range(100):
    if prime(i) == 1:
        print(i)














