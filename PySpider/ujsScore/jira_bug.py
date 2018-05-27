from jira import JIRA
import csv
import time
import os

class JiraData(object):
    """docstring for JiraData"""
    bug_trend=[]
    jira = ''
    start_date = '2015-03-15'
    curr_date = time.strftime("%Y-%m-%d", time.localtime())
    file_name = 'D:/python/bugstat/data/bug_trend.csv'

    def __init__(self):
        super(JiraData, self).__init__()
        self.jira = JIRA('http://localhost/jira/',basic_auth=('username', 'password'))
        #创建jira链接

    #获取bug趋势统计数据写入到csv文件中，追加
    def write_CSVFile(self, bug_data,file_type):
        with open(self.file_name, file_type, newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            spamwriter.writerow(bug_data)

    def get_bug_trend_data(self):


        if not os.path.exists(self.file_name):
            self.write_CSVFile(['create_date','All','Resolved','Closed'],'a')

        self.bug_trend.append(self.curr_date)
        self.bug_trend.append(len(self.jira.search_issues("project = VJFOUR AND issuetype = Bug AND created >= %s " %self.start_date)))
        self.bug_trend.append(len(self.jira.search_issues("project = VJFOUR AND issuetype = Bug AND status in (Resolved, Closed) AND created >= %s " %self.start_date)))
        self.bug_trend.append(len(self.jira.search_issues("project = VJFOUR AND issuetype = Bug AND status = Closed AND created >= %s " %self.start_date)))

        self.write_CSVFile(self.bug_trend,'a')


if __name__ == '__main__':
    jd = JiraData()
    jd.get_bug_trend_data()