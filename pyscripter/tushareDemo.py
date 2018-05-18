import tushare as ts
import os

code=input('股票代码:')
start=input('开始日期，格式YYYY-MM-DD:')
end=input('结束日期，格式YYYY-MM-DD:')
os.makedirs(r'%s/k线数据'%code)
os.makedirs(r'%s/复权数据'%code)

#历史行情数据
#k线数据
ts.get_hist_data(code=code,start=start,end=end, ktype='5').to_csv('%s/k线数据/5分钟.csv'%code) #5分钟
ts.get_hist_data(code=code,start=start,end=end, ktype='15').to_csv('%s/k线数据/15分钟.csv'%code) #15分钟
ts.get_hist_data(code=code,start=start,end=end, ktype='30').to_csv('%s/k线数据/30分钟.csv'%code) #30分钟
ts.get_hist_data(code=code,start=start,end=end, ktype='60').to_csv('%s/k线数据/60分钟.csv'%code) #60分钟
ts.get_hist_data(code=code,start=start,end=end).to_csv('%s/k线数据/月.csv'%int(code)) #日
ts.get_hist_data(code=code,start=start,end=end, ktype='W').to_csv('%s/k线数据/周.csv'%code) #周
ts.get_hist_data(code=code,start=start,end=end, ktype='M').to_csv('%s/k线数据/月.csv'%code) #月
ts.get_hist_data('sh',start=start,end=end).to_csv('%s/k线数据/上证指数.csv'%code) #上证指数
ts.get_hist_data('sz',start=start,end=end).to_csv('%s/k线数据/深圳成指.csv'%code) #深圳成指
ts.get_hist_data('hs300',start=start,end=end).to_csv('%s/k线数据/沪深300指数.csv'%code) #沪深300指数
ts.get_hist_data('sz50',start=start,end=end).to_csv('%s/k线数据/上证50指数.csv'%code) #上证50指数
ts.get_hist_data('zxb',start=start,end=end).to_csv('%s/k线数据/中小板指数.csv'%code) #中小板指数
ts.get_hist_data('cyb',start=start,end=end).to_csv('%s/k线数据/创业板指数.csv'%code) #创业板指数
#复权数据
ts.get_h_data(code=code,start=start,end=end).to_csv('%s/复权数据/前复权.csv'%code) #前复权
ts.get_h_data(code=code,start=start,end=end, autype='hfq').to_csv('%s/复权数据/后复权.csv'%code) #后复权
ts.get_h_data(code=code,start=start,end=end, autype=None).to_csv('%s/复权数据/不复权.csv'%code) #不复权
#实时行情数据
try:
    ts.get_today_all(code=code).to_csv('%s/实时行情数据.csv'%code)
except:
    print('找不到数据')
#大盘指数列表
ts.get_index().to_csv('%s/大盘指数行情列表.csv'%code)