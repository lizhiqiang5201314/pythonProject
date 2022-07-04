import logging
import schedule
import time
import random
from schedule import every, repeat, run_pending
from datetime import datetime
from apptest.dir import login

def job():
    print('运行中')
    login.py

job()

schedule.every().monday.at("08:45").do(job)
schedule.every().tuesday.at("20:54").do(job)
schedule.every().wednesday.at("08:52").do(job)
schedule.every().thursday.at("08:49").do(job)
schedule.every().friday.at("08:51").do(job)
# schedule.every(1).seconds.do(job)
# schedule.every().day.at('08:50').do(job)  # 每天八点半点运行

while True:
    schedule.run_pending()
    time.sleep(1)




schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)



dayOfWeek = datetime.now().isoweekday()  ###返回数字1-7代表周一到周日
# a = '08:3'  # 获取随机时间
b = random.randint(0, 9)
c = ("%s%d" % (a, b))
print(c)
def shijian():
    dayOfWeek = datetime.now().isoweekday() ###返回数字1-7代表周一到周日
    global a,b,c
    a = '08:3'                      #获取随机时间
    b = random.randint(0, 9)
    c = ("%s%d" % (a, b))
    print(c)
