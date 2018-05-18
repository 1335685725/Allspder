import re
string = "BTC 100081"

# match = re.search(r'[1-9]\d{5}',string)
# if match:
#     print(match.group(0))
'''match面向对象用法'''
# pat = re.compile(r'[1-9]\d{5}')
# rst = pat.match(string)



'''match函数式用法'''
# match = re.match(r'[1-9]\d{5}',"1004854 BTC")
# if match:
#     print(match.group(0))

# ls = re.findall(r'[1-9]\d{5}',"btc120000 das321654")
# print(ls)

# er = re.split(r'[1-9]\d{5}',"btc120000 das321654",maxsplit=1) #分割
# print(er)

# match = re.finditer(r'[1-9]\d{5}',"btc120000 das321654")
# for m in match:
#     if m:
#         print(m.group(0))

        #迭代
# match = re.sub(r'[1-9]\d{5}',repl="youbian",string="btc120000 das321654")
# print(match)




