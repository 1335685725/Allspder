import datetime

# 获取当前日期
today = datetime.datetime.now()
print(today)
# 获取当天的date
tod = datetime.date.today()
print(tod)
# 获取明天/前N天
tom = datetime.date.today() + datetime.timedelta(days=1)
print(tom)
# 三天前
nowday = datetime.datetime.now()
threedaysago = datetime.datetime.now() - datetime.timedelta(days=3)
print(threedaysago)
# 获取当天的开始时间和结束时间
starttime = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
endtime = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
print(starttime)
print(endtime)
# 获取两个datetime的时间差
cha = (datetime.datetime(2018, 4, 15, 12, 0, 0) - datetime.datetime.now()).total_seconds()
print(cha)
# 获取本周/本月/上月的最后一天
# 本周
today = datetime.date.today()
sunday = today + datetime.timedelta(6 - today.weekday())
# 本月
import calendar
_, last_day_num = calendar.monthrange(today.year, today.month)
last_day = datetime.date(today.year, today.month, last_day_num)
print(last_day)
# 上个月的最后一天
first = datetime.date(day=1, year=today.year, month=today.month) # 获取本月第一天
last_month = first - datetime.timedelta(days=1)
print(last_month)
# 关系转换
# datetime <==> string
# datetime -> str
str_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(str_now)
str_now = datetime.datetime.now().strftime("%D %H:%M:%S")
print(str_now)
# str -> datetime
date_t = datetime.datetime.strptime("2014-12-31 18:20:10", "%Y-%m-%d %H:%M:%S")
print(date_t)
stra = "abc"
print(stra[:-1])



