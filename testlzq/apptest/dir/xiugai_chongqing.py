#-*- coding:utf-8 -*-
import uiautomator2 as u2
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import os
from datetime import datetime,time
from time import sleep
import sys
import csv
from queue import Queue
import json
import requests
import shutil
import time
from apscheduler.schedulers.blocking import BlockingScheduler



fileName = datetime.now().strftime('day' + '%Y_%m_%d')
log_path = os.path.join(os.getcwd(),fileName+'.txt')
#数据路径存储，用来传输和数据处理
csv_result_path = os.path.join(os.getcwd(), "temp_monitor1.csv")
csv_result_path2 = os.path.join(os.getcwd(), "temp_monitor2.csv")
ruku_path = os.path.join(os.getcwd(), "competitor.csv")
start_time_path = os.path.join(os.getcwd(), "start_time.csv")
log_city_path = os.path.join(os.getcwd(), "city.txt")
log_error_city_path = os.path.join(os.getcwd(), "city_error.txt")
platfrom_path = os.path.join(os.getcwd(),"修正表.xlsx")
#存放目录用于查看
# data_path = os.path.join(os.getcwd(),'data_file')
data_file_path1 =os.path.join(os.getcwd(),"temp_monitor5.csv")
data_file_path2 = os.path.join(os.getcwd(),"temp_monitor3.csv")


data_path = r'C:\Users\86138\Desktop\Gaode\Fenbushi\fbs_guangdong\data_file\temp_monitor1.csv'
data_city_text_path = r'C:\Users\86138\Desktop\Gaode\Fenbushi\fbs_guangdong\data_file\city.txt'
data_city_error_path = r'C:\Users\86138\Desktop\Gaode\Fenbushi\fbs_guangdong\data_file\city_error.txt'

driver = u2.connect("g6jz5lhiv48xhu9p")

q = Queue(maxsize=6000)
print(q.qsize())
# 添加要爬取的异常数据
q_error = Queue(maxsize=6000)

class Logger(object):
    def __init__(self, filename="Test", path="./"):
        self.terminal = sys.stdout
        self.log = open(os.path.join(path, filename), "a", encoding='utf8', )

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

def write_spider_title():
    print("新建spider.csv标题文件")
    f = open(csv_result_path, 'w', encoding='utf-8')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["id","station_name","address","competitor_price","competitor_price2","type","state","oil_id","create_time","input_item","city"])
    f.close()

def write_spider_title2():
    print("新建spider.csv标题文件")
    f = open(csv_result_path2, 'w', encoding='utf-8')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["id","station_name","competitor_price","type_platform","state","create_time","input_item","city"])
    f.close()

def delete_file():
    try:
        print("开始清理文件")
        if os.path.exists(csv_result_path):
            os.remove(csv_result_path)
        if os.path.exists(log_city_path):
            os.remove(log_city_path)
        if os.path.exists(log_error_city_path):
            os.remove(log_error_city_path)
        if os.path.exists(ruku_path):
            os.remove(ruku_path)
        if os.path.exists(start_time_path):
            os.remove(start_time_path)
        if os.path.exists(csv_result_path2):
            os.remove(csv_result_path2)
        # if os.path.exists(log_path):
        #     os.remove(log_path)
        print("清理文件完成")
    except:
        print("清理文件失败")

def get_files():
    f = open("city.txt","a+")
    f.close()

def delete_tankuang():
    if driver(text="不再提示").exists:
        driver(text="不再提示").click()
        sleep(1)
        driver(text="暂不开启").click()

def delete_tankuang2():
    if driver.xpath('//*[@resource-id="com.autonavi.minimap:id/iv_close"]').exists:
        driver.click(0.79, 0.226)

def delete_tankuang8():
    if driver.xpath('//*[@resource-id="com.autonavi.minimap:id/iv_close"]').exists:
        driver.click(0.785, 0.229)

def delete_tankuang3():
    try:
        if driver.xpath('//*[@resource-id="com.autonavi.minimap:id/button1"]').exists:
            if driver.xpath('//*[@resource-id="com.autonavi.minimap:id/button1"]').get_text() == "忽略":
                print("启动时候出现升级弹框")
                driver(text="忽略").click()
                sleep(2)
    except Exception as e:
        print("当前处理启动弹框异常，此处略过:%s"%(e))
        pass

def get_time():
    otherStyleTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return otherStyleTime

def sql_time():
    otherStyleTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return otherStyleTime

#新增启动弹出框判断
def delete_qd_tc():
    if driver(text = 'ADAS功能全新上线').exists:
        driver.click(0.785, 0.228)
        sleep(2)

#这里加载火车站经常卡死，判断如果10秒钟还在加载中，那么多等40秒
def deal_jiazai():
    if driver(text="加载中...").exists:
        sleep(40)

def tankuang_jage():
    if driver.xpath('//*[@resource-id="com.autonavi.minimap:id/mapInteractiveRelativeLayout"]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ImageView[1]').exists:
        print("出现弹框开始点击叉叉")
        driver.click(0.502, 0.765)
        print("已点击删除弹框")
        sleep(3)

#解析列表网页内容
def get_data_list(t,k,input_item,city_name):
    # global dongguan_list
    tankuang_jage()
    data_list = []
    if k == 1:
        for i in range(3,6):
            print("%s：阿炳真帅"%(i))
            data_dic = {}
            try:
                if driver.xpath('//android.support.v7.widget.RecyclerView/android.view.ViewGroup[{}]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View[1]'.format(i)).exists:
                    data_dic["station_name"] =t+'-'+driver.xpath('//android.support.v7.widget.RecyclerView/android.view.ViewGroup[{}]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View[1]'.format(i)).get_text()
                    #这里新增地址
                    data_dic["address"] = driver.xpath('//android.support.v7.widget.RecyclerView/android.view.ViewGroup[{}]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.View[2]'.format(i)).get_text()
                    data_dic["competitor_price"] = "92#"+'¥'+driver.xpath('//android.support.v7.widget.RecyclerView/android.view.ViewGroup[{}]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.View[3]'.format(i)).get_text() +'/L'
                    data_dic["competitor_price2"] = driver.xpath(
                        '//android.support.v7.widget.RecyclerView/android.view.ViewGroup[{}]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.View[3]'.format(
                            i)).get_text()
                    data_dic["type"] = "6"
                    data_dic["state"] = "1"
                    data_dic["oil_id"] = "1"
                    data_dic["create_time"] = get_time()
                    data_dic["input_item"] = input_item
                    data_dic["city"] = city_name

            except Exception as e:
                print(e)
                pass
            if len(data_dic) ==10:
                data_list.append(data_dic)
                # dongguan_list.append(data_dic)
            print(data_dic)
            print("==================")
    else:
        for i in range(2, 7):
            print("%s：阿炳真帅气---" % (i))
            data_dic = {}
            try:
                # if driver.xpath('//android.support.v7.widget.RecyclerView/android.view.ViewGroup[{}]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View[1]'.format(i)).exists:
                data_dic["station_name"] = t+'-'+driver.xpath(
                    '//android.support.v7.widget.RecyclerView/android.view.ViewGroup[{}]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View[1]'.format(
                        i)).get_text()
                # 这里新增地址
                data_dic["address"] = driver.xpath(
                    '//android.support.v7.widget.RecyclerView/android.view.ViewGroup[{}]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.View[2]'.format(i)).get_text()
                data_dic["competitor_price"] = "92#"+'¥'+driver.xpath(
                    '//android.support.v7.widget.RecyclerView/android.view.ViewGroup[{}]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.View[3]'.format(
                        i)).get_text()+'/L'
                data_dic["competitor_price2"] = driver.xpath(
                    '//android.support.v7.widget.RecyclerView/android.view.ViewGroup[{}]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.view.View[3]'.format(
                        i)).get_text()
                data_dic["type"] = "6"
                data_dic["state"] = "1"
                data_dic["oil_id"] = "1"
                data_dic["create_time"] = get_time()
                data_dic["input_item"] = input_item
                data_dic["city"] = city_name

            except Exception as e:
                print(e)
                pass
            if len(data_dic) == 9:
                data_list.append(data_dic)
                # dongguan_list.append(data_dic)
            print(data_dic)
            print("==================")
    deal_dong_list(data_list)

def deal_dong_list(data):
    try:
        df = pd.DataFrame(data)
        df["id"] = '0'
        df_sx = df[["id","station_name","address","competitor_price","competitor_price2","type","state","oil_id","create_time","input_item","city"]]

        data2 = df_sx.rename(columns={"type":"type_platform"})[["id","station_name","competitor_price","type_platform","state","create_time","input_item","city"]]
        df_sx.to_csv("temp_monitor1.csv",index=None,encoding="utf-8",mode='a',header=None)
        data2.to_csv("temp_monitor2.csv",index=None,encoding="utf-8",mode='a',header=None)

    except Exception as e:
        print(e)
        pass

def main(t,input_item,city_name):
    k = 0
    while True:
        k = k+1
        print("正在解析第%s页"%(k))
        sleep(1)
        get_data_list(t,k,input_item,city_name)
        break
        # driver.swipe(0.094, 0.862, 0.094, 0.222)
        # if driver.xpath('//*[@text="网络异常，点击重新加载"]').exists:
        #     driver.click(0.537, 0.923)
        #     sleep(2)
        # if driver(text="没有更多结果了").exists:
        #     get_data_list(t,k,input_item)
        #     print("深圳数据爬取完毕")
        #     print("程序结束時間:%s" %(datetime.now()))
        #     break
    print("测试完毕开始返回")
    driver.press("back")
    sleep(2)
    if driver(text="附近").exists:
        print("测试完成")
    else:
        sleep(2)
        driver.press("back")
    driver(scrollable=True).scroll.toBeginning()

#记录爬取完成的城市
def write_city(kt):
    with open("city.txt","a+",encoding="utf8") as f:
        f.write("%s"%(kt))
        f.write("\n")

def write_city_error(kt):
    with open("city_error.txt","a+",encoding="utf8") as f:
        f.write("%s"%(kt))
        f.write("\n")

def push_zuobiao():
    global q
    print("step1:开始获取城市坐标数据")
    path = os.path.join(os.getcwd(), "城市选点列表.xlsx")
    data = pd.read_excel(path)[["城市","输入项","点击项"]][0:275]
    data["status"] = 1
    data2 = data.groupby("status").apply(lambda y: list(zip(y["城市"], y["输入项"], y["点击项"])))[1]
    print(data2)
    for i in data2:
        q.put(i)

# #中间判断队列
# def innde_dec_queue():
#     global q,q_error
#     if q.qsize()>0:
#         print("当前存储队列需爬取数:%s"%(q.qsize()))
#         t = q.get()
#         return t
#     elif q.qsize()==0 and q_error.qsize()>0:
#         print("当前异常队列需要爬取数为:%s"%(q_error.qsize()))
#         t = q_error.get()
#         return t
#     else:
#         return


#攀枝花
def get_panzhihua_data():
    print("开始执行正常任务队列")
    global q,q_error
    if q.qsize() ==0:
        print("正常任务队列数据爬取完毕")
        return
    zuobiao_data = q.get()
    print("当前对列大小为:%s"%q.qsize())
    print(zuobiao_data)
    print(type(zuobiao_data))
    print("当前获取爬取信息:%s"%(str(zuobiao_data)))
    input_tb = 0
    city_tb = 0
    city_name = zuobiao_data[0]
    input_item = zuobiao_data[1]
    click_item = zuobiao_data[2]
    #头部成名名
    if '市' in city_name:
        city_tb = city_name.replace('市', '')
        input_tb = input_item.split('市')[1]
    elif '州' in city_name:
        city_tb = city_name.split("州")[0][0:2]+"州"
        input_tb = city_name.split("州")[1]
    print("==============================")
    print(city_tb,input_tb)
    try:
        driver(scrollable=True).scroll.toBeginning()
        sleep(2)
        print("开始测试%s城市的数据"%(city_name))
        print("%s爬取开始時間:%s" % (city_name,datetime.now()))
        #点击下拉框
        if driver.xpath('//*[@resource-id="com.autonavi.minimap:id/fragment_container"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]').exists:

            try:
                driver.xpath(
                    '//*[@resource-id="com.autonavi.minimap:id/fragment_container"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]').click()
                print("step1:下拉框存在，开始点击下拉框")
                sleep(1)
                if driver(text="切换地点").exists:
                    pass
                else:
                    print("error:没有看到关键字，现在开始点击坐标")
                    driver.click(0.323, 0.068)
                    print("step1:坐标点击下拉框完成，开始选择字母")

            except:
                print("step1:(2)点击下拉框出问题，开始点击坐标")
                driver.click(0.323, 0.068)
                print("step1:点击下拉框完成，开始选择字母")
        sleep(1)
        if driver(text="当前城市").exists:
            driver(text="当前城市").click()
            print("step3:选择城市完成，开始选择火车站")
        else:
            if driver(text="S").exists:
                driver(text="S").click()
                print("step2:选择字母完成,开始选择城市")
            sleep(1)
            if driver(text="深圳市").exists:
                driver(text="深圳市").click()
                print("step3:选择城市完成，开始选择火车站")
        sleep(2)
        deal_jiazai()
        if driver(text="中文/拼音/首字母").exists:
            print("这个框框出现，开始输入加油站")
            # driver.set_fastinput_ime(True)
            #输入项
            driver(focused=True).send_keys(input_item)
            sleep(4)
            #点击项
            if driver(text=click_item).exists:
                print("点击项:%s"%(click_item))
                driver(text=click_item).click()
            else:
                driver.click(0.158, 0.12)
        sleep(2)
        driver(scrollable=True).scroll.toBeginning()
        sleep(2)
        driver.implicitly_wait(10)
        #判断城市是否是东莞，如果是就点击加油站加载加油站列表
        #头部显示
        if driver.xpath(
                '//*[@resource-id="com.autonavi.minimap:id/fragment_container"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View[1]').get_text() == city_tb or driver.xpath(
            '//*[@resource-id="com.autonavi.minimap:id/fragment_container"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View[1]').get_text() == input_tb:
            print("页面显示是湛江加油站城市列表，开始加载湛江城市加油站页面")
            print("=================================================")
            try:
                if driver.xpath('//*[@text="加油站"]').get_text()=="加油站":
                    driver(text="加油站").click()
                    print("step5:点击加油站成功,等待油站列表页加载")
            except:
                print("step5:点击异常,等待2秒后重新加载")
                sleep(2)
                driver(text="加油站").click()
            driver.implicitly_wait(20)
            # tankuang_jage()
            try:
                if driver.xpath('//*[@resource-id="com.autonavi.minimap:id/mapInteractiveRelativeLayout"]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ImageView[1]').exists:
                    print("出现弹框开始点击叉叉")
                    driver.click(0.502, 0.765)
                    print("已点击删除弹框")
                    sleep(2)
            except:
                print("弹框不存在")
                sleep(2)

            tankuang_jage()
            #一般进来默认是92#，如果不是92#就不做页面接卸
            print(driver.xpath('//*[@text="92#"]').get_text())
            if driver.xpath('//*[@text="92#"]').exists:
                try:
                    if driver(text="<font color=&apos;#00000099&apos; size=&apos;24px&apos;><strong>优惠油站</strong></font>").exists:
                        driver(text="<font color=&apos;#00000099&apos; size=&apos;24px&apos;><strong>优惠油站</strong></font>").click()
                        driver.click(0.707, 0.232)
                        print("step:点击优惠加油完成,准备滑动1")
                except:
                    #点击优惠加油
                    print("step6:优惠加油这里的字段属性有变化，开始点击坐标")
                    driver.click(0.707, 0.232)
                    print("step:点击优惠加油完成,准备滑动2")

                sleep(2)
                if driver.xpath('//*[@text="汽油92#"]').exists:
                    driver.swipe(0.094, 0.34, 0.094, 0.178)
                    print("step7:滑动完成开始滑动和解析页面内容")
                    t=city_name+"区"
                    main(t,input_item,city_name)
                    print("%s城市数据爬取完成"%(city_tb))
                    print("%s爬取结束時間:%s" % (city_tb,datetime.now()))
                    write_city(input_item)
                else:
                    print("error:当前%s优惠加油页面，重新点击"%(city_tb))
                    driver.click(0.707, 0.232)
                    sleep(2)
                    driver.swipe(0.094, 0.34, 0.094, 0.178)
                    print("step7:滑动完成开始滑动和解析页面内容")
                    t = city_name + "区"
                    main(t,input_item,city_name)
                    print("%s城市数据爬取完成"%(city_tb))
                    print("%s爬取结束時間:%s" % (city_tb,datetime.now()))
                    write_city(input_item)
            else:
                print("error:当前没有进入%s加油站页面，点击失效重新点击"%(city_name))
                if driver.xpath('//*[@text="加油站"]').exists:
                    driver.click(0.885, 0.165)
                    sleep(2)
                tankuang_jage()
                if driver.xpath('//*[@text="92#"]').exists:
                    try:
                        if driver(
                                text="<font color=&apos;#00000099&apos; size=&apos;24px&apos;><strong>优惠油站</strong></font>").exists:
                            driver(
                                text="<font color=&apos;#00000099&apos; size=&apos;24px&apos;><strong>优惠油站</strong></font>").click()
                            print("step:点击优惠加油完成,准备滑动1")
                    except:
                        # 点击优惠加油
                        print("step6:优惠加油这里的字段属性有变化，开始点击坐标")
                        driver.click(0.707, 0.232)
                        print("step:点击优惠加油完成,准备滑动2")

                    sleep(2)
                    if driver.xpath('//*[@text="汽油92#"]').exists:
                        driver.swipe(0.094, 0.34, 0.094, 0.178)
                        print("step7:滑动完成开始滑动和解析页面内容")
                        t = city_name + "区"
                        main(t,input_item,city_name)
                        print("%s城市数据爬取完成"%(city_tb))
                        print("%s爬取结束時間:%s" % (city_tb,datetime.now()))
                        write_city(input_item)
                    else:
                        print("error:当前不是%s优惠加油页面，现在重新点击优惠加油"%(city_tb))
                        driver.click(0.707, 0.232)
                        sleep(2)
                        driver.swipe(0.094, 0.34, 0.094, 0.178)
                        print("step7:滑动完成开始滑动和解析页面内容")
                        t = city_name + "区"
                        main(t,input_item,city_name)
                        print("%s城市数据爬取完成"%(city_tb))
                        print("%s爬取结束時間:%s" % (city_tb,datetime.now()))
                        write_city(input_item)
                else:
                    print("error:%s城市92#不存在点击坐标数据也没有加载成功"%(city_name))
        # else:
        #     q_error.put(zuobiao_data)
        #     return
    except:
        write_city_error(input_item)
        # q_error.put(zuobiao_data)
        hui_sucess()
        pass

#攀枝花
def get_panzhihua_data_error():
    print("开始执行异常任务队列")
    global q_error
    if q_error.qsize()==0:
        print("队列数据爬取完毕")
        return
    zuobiao_data = q_error.get()
    print("当前对列大小为:%s"%q.qsize())
    print(zuobiao_data)
    print(type(zuobiao_data))
    print("当前获取爬取信息:%s"%(str(zuobiao_data)))
    city_name = zuobiao_data[0]
    input_item = zuobiao_data[1]
    click_item = zuobiao_data[2]
    city_tb = 0
    input_tb = 0
    #头部成名名
    if '市' in city_name:
        city_tb = city_name.replace('市', '')
        input_tb = input_item.split('市')[1]
    elif '州' in city_name:
        city_tb = city_name.split("州")[0][0:2]+"州"
        input_tb = city_name.split("州")[1]

    print("==============================")
    print(city_tb,input_tb)
    try:
        driver(scrollable=True).scroll.toBeginning()
        sleep(2)
        print("开始测试%s城市的数据"%(city_name))
        print("%s爬取开始時間:%s" % (city_name,datetime.now()))
        #点击下拉框
        if driver.xpath('//*[@resource-id="com.autonavi.minimap:id/fragment_container"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]').exists:
            try:
                driver.xpath(
                    '//*[@resource-id="com.autonavi.minimap:id/fragment_container"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]').click()
                print("step1:下拉框存在，开始点击下拉框")
                sleep(1)
                if driver(text="切换地点").exists:
                    pass
                else:
                    print("error:没有看到关键字，现在开始点击坐标")
                    driver.click(0.323, 0.068)
                    print("step1:坐标点击下拉框完成，开始选择字母")

            except:
                print("step1:(2)点击下拉框出问题，开始点击坐标")
                driver.click(0.323, 0.068)
                print("step1:点击下拉框完成，开始选择字母")
        sleep(1)
        if driver(text="当前城市").exists:
            driver(text="当前城市").click()
            print("step3:选择城市完成，开始选择火车站")
        sleep(2)
        deal_jiazai()
        if driver(text="中文/拼音/首字母").exists:
            print("这个框框出现，开始输入加油站")
            # driver.set_fastinput_ime(True)
            #输入项
            driver(focused=True).send_keys(input_item)
            sleep(4)
            #点击项
            if driver(text=click_item).exists:
                print("点击项:%s"%(click_item))
                driver(text=click_item).click()
            else:
                driver.click(0.158, 0.12)
        sleep(2)
        driver(scrollable=True).scroll.toBeginning()
        sleep(2)
        # driver.implicitly_wait(10)
        #判断城市是否是东莞，如果是就点击加油站加载加油站列表
        #头部显示
        if driver.xpath(
                '//*[@resource-id="com.autonavi.minimap:id/fragment_container"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View[1]').get_text() == city_tb or driver.xpath(
            '//*[@resource-id="com.autonavi.minimap:id/fragment_container"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View[1]').get_text() == input_tb:
            print("页面显示是湛江加油站城市列表，开始加载湛江城市加油站页面")
            print("=================================================")
            try:
                if driver.xpath('//*[@text="加油站"]').get_text()=="加油站":
                    driver(text="加油站").click()
                    print("step5:点击加油站成功,等待油站列表页加载")
            except:
                print("step5:点击异常,等待2秒后重新加载")
                sleep(2)
                driver(text="加油站").click()
            driver.implicitly_wait(20)
            # tankuang_jage()
            try:
                if driver.xpath('//*[@resource-id="com.autonavi.minimap:id/mapInteractiveRelativeLayout"]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ImageView[1]').exists:
                    print("出现弹框开始点击叉叉")
                    driver.click(0.502, 0.765)
                    print("已点击删除弹框")
                    sleep(2)
            except:
                print("弹框不存在")
                sleep(2)

            tankuang_jage()
            #一般进来默认是92#，如果不是92#就不做页面接卸
            print(driver.xpath('//*[@text="92#"]').get_text())
            if driver.xpath('//*[@text="92#"]').exists:
                try:
                    if driver(text="<font color=&apos;#00000099&apos; size=&apos;24px&apos;><strong>优惠油站</strong></font>").exists:
                        driver(text="<font color=&apos;#00000099&apos; size=&apos;24px&apos;><strong>优惠油站</strong></font>").click()
                        driver.click(0.707, 0.232)
                        print("step:点击优惠加油完成,准备滑动1")
                except:
                    #点击优惠加油
                    print("step6:优惠加油这里的字段属性有变化，开始点击坐标")
                    driver.click(0.707, 0.232)
                    print("step:点击优惠加油完成,准备滑动2")

                sleep(2)
                if driver.xpath('//*[@text="汽油92#"]').exists:
                    driver.swipe(0.094, 0.34, 0.094, 0.178)
                    print("step7:滑动完成开始滑动和解析页面内容")
                    t=city_name+"区"
                    main(t,input_item,city_name)
                    print("%s城市数据爬取完成"%(city_tb))
                    print("%s爬取结束時間:%s" % (city_tb,datetime.now()))
                    write_city(input_item)
                else:
                    print("error:当前%s优惠加油页面，重新点击"%(city_tb))
                    driver.click(0.707, 0.232)
                    sleep(2)
                    driver.swipe(0.094, 0.34, 0.094, 0.178)
                    print("step7:滑动完成开始滑动和解析页面内容")
                    t = city_name + "区"
                    main(t,input_item,city_name)
                    print("%s城市数据爬取完成"%(city_tb))
                    print("%s爬取结束時間:%s" % (city_tb,datetime.now()))
                    write_city(input_item)
            else:
                print("error:当前没有进入%s加油站页面，点击失效重新点击"%(city_name))
                if driver.xpath('//*[@text="加油站"]').exists:
                    driver.click(0.885, 0.165)
                    sleep(2)
                tankuang_jage()
                if driver.xpath('//*[@text="92#"]').exists:
                    try:
                        if driver(
                                text="<font color=&apos;#00000099&apos; size=&apos;24px&apos;><strong>优惠油站</strong></font>").exists:
                            driver(
                                text="<font color=&apos;#00000099&apos; size=&apos;24px&apos;><strong>优惠油站</strong></font>").click()
                            print("step:点击优惠加油完成,准备滑动1")
                    except:
                        # 点击优惠加油
                        print("step6:优惠加油这里的字段属性有变化，开始点击坐标")
                        driver.click(0.707, 0.232)
                        print("step:点击优惠加油完成,准备滑动2")

                    sleep(2)
                    if driver.xpath('//*[@text="汽油92#"]').exists:
                        driver.swipe(0.094, 0.34, 0.094, 0.178)
                        print("step7:滑动完成开始滑动和解析页面内容")
                        t = city_name + "区"
                        main(t,input_item,city_name)
                        print("%s城市数据爬取完成"%(city_tb))
                        print("%s爬取结束時間:%s" % (city_tb,datetime.now()))
                        write_city(input_item)
                    else:
                        print("error:当前不是%s优惠加油页面，现在重新点击优惠加油"%(city_tb))
                        driver.click(0.707, 0.232)
                        sleep(2)
                        driver.swipe(0.094, 0.34, 0.094, 0.178)
                        print("step7:滑动完成开始滑动和解析页面内容")
                        t = city_name + "区"
                        main(t,input_item,city_name)
                        print("%s城市数据爬取完成"%(city_tb))
                        print("%s爬取结束時間:%s" % (city_tb,datetime.now()))
                        write_city(input_item)
                else:
                    print("error:%s城市92#不存在点击坐标数据也没有加载成功"%(city_name))
        else:
            pass
    except :
        write_city_error(input_item)
        hui_sucess()
        print("异常出现，函数运行结束")
        pass

#这里写个函数帮助回到正确的页面
def hui_sucess():
    if driver(text="附近").exists:
        print("测试完成")
    else:
        sleep(2)
        driver.press("back")
    driver(scrollable=True).scroll.toBeginning()

def panzhihua_fz_error():
    print("开始执行异常任务队列")
    global q, q_error
    while True:
        if q_error.qsize() == 0:
            return
        try:
            if driver(text="我的").exists:
                print("当前页面是爬取正常页面，开始爬取广州城市数据")
                if driver(text="附近").exists:
                    driver(text="附近").click()
                get_panzhihua_data_error()

            elif driver(text="机场火车站").exists:
                driver.press("back")
                sleep(1)
                driver.press("back")
                get_panzhihua_data_error()
            elif driver(text="切换地点").exists:
                driver.press("back")
                get_panzhihua_data_error()
            else:
                driver.press("back")
                sleep(1)
                driver.press("back")
                sleep(1)
                driver.press("back")
                get_panzhihua_data_error()
        except Exception as e:
            print("error:深圳城市爬取出现异常，未爬取:%s" % (e))
            pass
    pass
#攀枝花
def panzhihua_fz():
    global q
    while True:
        if q.qsize()==0:
            print("当前正常队列结束,开始异常队列爬取")
            return
        try:
            del_tankuang()
            if driver(text="我的").exists:
                print("当前页面是爬取正常页面，开始爬取广州城市数据")
                if driver(text="附近").exists:
                    driver(text="附近").click()
                get_panzhihua_data()
            elif driver(text="机场火车站").exists:
                driver.press("back")
                sleep(1)
                driver.press("back")
                if driver(text="附近").exists:
                    driver(text="附近").click()
                get_panzhihua_data()
            elif driver(text="切换地点").exists:
                driver.press("back")
                if driver(text="附近").exists:
                    driver(text="附近").click()
                get_panzhihua_data()
            else:
                driver.app_stop(package_name='com.autonavi.minimap')
                sleep(2)
                driver.app_start(package_name='com.autonavi.minimap',
                                 activity='com.autonavi.map.activity.NewMapActivity')
                if driver(text="本次运行允许").exists:
                    print("有弹出框：本次允许运行")
                    driver(text="本次运行允许").click()
                    print("弹出框点击完毕")
                sleep(2)
                delete_tankuang()
                delete_tankuang2()
                # 升级弹框
                delete_tankuang3()
                sleep(3)
                delete_tankuang8()
                sleep(2)
                delete_qd_tc()
                if driver(text="附近").exists:
                    driver(text="附近").click()
                    get_panzhihua_data()
                # driver.press("back")
                # sleep(1)
                # driver.press("back")
                # sleep(1)
                # # driver.press("back")
                # if driver(text="附近").exists:
                #     driver(text="附近").click()
                #     get_panzhihua_data()
        except Exception as e:
            print("error:深圳城市爬取出现异常，未爬取:%s"%(e))
            pass

###########################################################################
def chu2(x):
    y = {}
    y["id"] = x[0]
    y["station_id"] = x[1]
    y["competitor_price"] = x[2]
    y["oil_id"] = x[3]
    y["type"] = x[4]
    y["show_type"] = x[5]
    y["isxy"] = x[6]
    y["longitude"] = x[7]
    y["latitude"] = x[8]
    y["state"] = x[9]
    y["create_time"] = x[10]
    y["update_time"] = x[11]
    y["updater_batch_num"] = x[12]
    return y

def chuli_dict2(x):
    y = [chu2(i) for i in x]
    return y
#上传monitor表文件
def upload_file_monitor():
    print("开始上传重叠表文件")
    chunks = pd.read_csv(ruku_path, encoding="utf-8")
    data = chunks.groupby("state").apply(lambda y: list(zip(y["id"], y["station_id"], y["competitor_price"],
                                                            y["oil_id"], y["type"], y["show_type"], y["isxy"],
                                                            y["longitude"], y["latitude"], y["state"],
                                                            y["create_time"], y["update_time"],y["updater_batch_num"])))[1]
    data1 = chuli_dict2(data)
    data2 = json.dumps(data1)
    # print(data2)
    try:
        url = "https://api.ejiayou.com/ejy-station-center-service/autoPriceAdjust/competitorMonitor/import/data/json"
        headers = {"Content-Type": "application/json"}
        r = requests.post(url, headers=headers, data=data2, verify=False)
        if r.status_code == 200:
            print("传入chongdie2.csv表文件到java后端成功")
            print(r.json())
        print(r.status_code)
    except Exception as e:
        print("error:%s" % (e))
        pass

#上传start_time表文件
def upload_file_start_time():
    try:
        print("开始上传start_time.csv表")
        data = pd.read_csv(start_time_path, encoding="utf-8")
        data_list = []
        datal = {}
        datal["id"] = str(data.loc[0]["id"])
        datal["start_time"] = data.loc[0]["start_time"]
        print(datal)
        data_list.append(datal)
        # print(data_list)
        datal_json = json.dumps(data_list)
        # print(datal_json)
        #
        url = "https://api.ejiayou.com/ejy-base-data-service/file/import/data/json/activity_competitor_monitor_start_time"
        headers = {"Content-Type": "application/json"}
        r = requests.post(url, headers=headers, data=datal_json, verify=False)

        if r.status_code == 200:
            print("传入start_time.csv表文件到java后端成功")
            print(r.json())
        print(r.status_code)
    except Exception as e:
        print("入库start_time.csv失败:%s"%(e))
        pass

def deal_start_time():
    try:
        now_time = get_time()
        print("当前更新的start_time时间为:%s" % (now_time))
        # engine2 = create_engine('mysql+pymysql://gaode_spider:lcsT3tJS4MW98OmTzt8bWjIZ@rr-bp1od7a429zn9v1h1363.mysql.rds.aliyuncs.com:3306/yijiayou?charset=utf8')
        # sql = ' select * from activity_competitor_monitor_start_time where platform_type=6'
        engine2 = create_engine('mysql+pymysql://gaode_spider:lcsT3tJS4MW98OmTzt8bWjIZ@rr-bp1od7a429zn9v1h1363.mysql.rds.aliyuncs.com:3306/yijiayou?charset=utf8')
        sql = ' select * from activity_competitor_monitor_start_time where platform_type=6'
        data8 = pd.read_sql(sql, con=engine2)
        data8["start_time"] = get_time()
        data8.to_csv("start_time.csv", index=None, encoding="utf-8")
        upload_file_start_time()
    except Exception as e:
        print("error:%s"%e)

def deal_to_sql():

    try:
        deal_start_time()
        print("step1:打印爬虫爬取数据")
        data_cd = pd.read_csv("temp_monitor1.csv").dropna()
        data_cd["station_name"] = data_cd["station_name"].apply(lambda x: x.split("-")[1])
        data_df = data_cd.drop_duplicates(subset=["address","station_name"])[
            ["station_name", "type", "competitor_price2","address","city"]]
        data_df = data_df.rename(columns={"competitor_price2": "competitor_price"})
        data_df["type"].apply(lambda x: str(x))
        print("step1:修改后的爬虫数据量:")
        print(data_df.shape[0])
        print("==========================")

        print("step2:获取修正STATION_ID表的数据")
        #这里修改，匹配增加了地址
        sql = pd.read_excel(platfrom_path).drop_duplicates(subset=["address", "station_name"])[
            ["station_id", "station_name","city", "address"]]
        data2 = sql.dropna()
        print("station_id表的数据量:")
        print(data2.shape[0])
        print("=====================")

        print("step3:合并爬虫表和staition_id表数据")
        # data3 = pd.merge(data_df, data2, on=["station_name","address"], how="left").dropna()
        #这里油站名称由station_name,address改为city,station_name
        data3 = pd.merge(data_df, data2, on=["station_name", "city"]).dropna()
        data3["oil_id"] = 1
        data3 = data3.reset_index()[
            ["station_id", "type", "oil_id", "competitor_price","city"]]
        print("这是匹配activity_competitor_platform_station_temp表获取station_id后的数据")
        print("这是要入库的总数量")
        print(data3.shape[0])



        print("step4:获取filling_station表数据")
        engine = create_engine('mysql+pymysql://gaode_spider:lcsT3tJS4MW98OmTzt8bWjIZ@rr-bp1od7a429zn9v1h1363.mysql.rds.aliyuncs.com:3306/yijiayou?charset=utf8')
        sql = 'SELECT * FROM yijiayou_filling_station'
        data4 = pd.read_sql(sql, con=engine).rename(
            columns={"filling_station_id": "station_id", "filling_longitude": "longitude", "filling_latitude": "latitude"})[
            ["station_id", "longitude", "latitude", "state"]]
        data4 = data4[data4.state == '1']
        print("这是filling_station表的数据量:")
        print(data4.shape[0])
        print("======================")
        #
        print("step5:获取filling_station表和爬虫data3表交集")
        data5 = pd.merge(data3, data4, on=['station_id'],how="left")
        print(data5.shape[0])
        #

        print("step6:获取重叠油站表数据")
        engine = create_engine('mysql+pymysql://gaode_spider:lcsT3tJS4MW98OmTzt8bWjIZ@rr-bp1od7a429zn9v1h1363.mysql.rds.aliyuncs.com:3306/yijiayou?charset=utf8')

        sql = 'SELECT * FROM activity_competitor_monitor'
        data6 = pd.read_sql(sql, con=engine)[["station_id", "oil_id", "type", "show_type", "isxy","id","auto_input"]].drop_duplicates(
            subset=['station_id','type','oil_id'])
        data6 = data6[data6["auto_input"] == 1]
        print("这是monitormator表的数据liang")
        print(data6.shape[0])
        print("======================")
        #
        #
        print("step7:合并filling_station表数据和重叠油价表数据")
        data7 = pd.merge(data5, data6, on=["station_id", "oil_id", "type"], how='left')[
            ["id","station_id","competitor_price", "oil_id", "type", "show_type", "isxy", "longitude", "latitude", "state"]].fillna('0')
        data7["create_time"] = sql_time()
        data7["update_time"] = sql_time()
        data7["state"] = 1
        data7["updater_batch_num"] = str(time.strftime('%Y%m%d%H%M%S', time.localtime()))
        # data7["id"] = '1'
        print("aaaaa")
        print(data7.shape[0])
        data7.to_csv("competitor.csv",index=None,encoding="utf-8")
        print(data7.columns.values)
        upload_file_monitor()


    except Exception as e:
        print("插入数据不成功:error:%s"%e)
        pass
# def deal_to_sql():
#
#     try:
#         deal_start_time()
#         print("step1:打印爬虫爬取数据")
#         data_cd = pd.read_csv("temp_monitor1.csv").dropna()
#         data_cd["station_name"] = data_cd["station_name"].apply(lambda x: x.split("-")[1])
#         data_df = data_cd.drop_duplicates(subset=["address","station_name"])[
#             ["station_name", "type", "competitor_price2","address"]]
#         data_df = data_df.rename(columns={"competitor_price2": "competitor_price"})
#         data_df["type"].apply(lambda x: str(x))
#         print("step1:修改后的爬虫数据量:")
#         print(data_df.shape[0])
#         print("==========================")
#
#         print("step2:获取STATION_ID表的数据")
#         try:
#             sql = pd.read_excel(platfrom_path).drop_duplicates(subset=["address", "station_name"])[
#                 ["station_id", "station_name", "address"]]
#             data2 = sql.dropna()
#             print("station_id表的数据量:")
#             print(data2.shape[0])
#             print("=====================")
#         except Exception as e:
#             print("error: %s"%(e))
#
#         try:
#             print("step3:合并爬虫表和staition_id表数据")
#             # data3 = pd.merge(data_df, data2, on=["station_name", "address"], how="left").dropna()
#             data3 = pd.merge(data_df, data2, on=["station_name","address"], how="left").dropna()
#             data3["oil_id"] = 1
#             data3 = data3.reset_index()[
#                 ["station_id", "type", "oil_id", "competitor_price"]]
#             print("这是匹配activity_competitor_platform_station_temp表获取station_id后的数据")
#             print(data3.shape[0])
#         except Exception as e:
#             print("error:合并爬虫表和staition_id表数据:%s"%(e))
#
#         print("step4:获取filling_station表数据")
#         engine = create_engine('mysql+pymysql://gaode_spider:lcsT3tJS4MW98OmTzt8bWjIZ@rr-bp1od7a429zn9v1h1363.mysql.rds.aliyuncs.com:3306/yijiayou?charset=utf8')
#         try:
#             sql = 'SELECT * FROM yijiayou_filling_station'
#             data4 = pd.read_sql(sql, con=engine).rename(
#                 columns={"filling_station_id": "station_id", "filling_longitude": "longitude", "filling_latitude": "latitude"})[
#                 ["station_id", "longitude", "latitude", "state"]]
#
#             # data4 = data4[data4.state != '0']
#             print("这是filling_station表的数据量:")
#             print(data4.shape[0])
#             print("======================")
#
#             print("step5:获取filling_station表和爬虫data3表交集")
#             data5 = pd.merge(data3, data4, on=['station_id'])
#             # data5 = data5[data5.state != '0']
#             print(data5.shape[0])
#         except Exception as e:
#             print("error:step5:获取filling_station表和爬虫data3表交集:%s"%(e))
#
#
#
#         try:
#             print("step6:获取重叠油站表数据")
#             engine = create_engine('mysql+pymysql://gaode_spider:lcsT3tJS4MW98OmTzt8bWjIZ@rr-bp1od7a429zn9v1h1363.mysql.rds.aliyuncs.com:3306/yijiayou?charset=utf8')
#
#             sql = 'SELECT * FROM activity_competitor_monitor'
#             data6 = pd.read_sql(sql, con=engine)[["station_id", "oil_id", "type", "show_type", "isxy","id"]].drop_duplicates(
#                 subset=['station_id','type','oil_id'])
#             print("这是monitormator表的数据liang")
#             print(data6)
#             print("======================")
#         except Exception as e:
#             print("error:step6:获取重叠油站表数据：%e"%(e))
#         try:
#             print("step7:合并filling_station表数据和重叠油价表数据")
#             data7 = pd.merge(data5, data6, on=["station_id", "oil_id", "type"], how='left')[
#                 ["id","station_id","competitor_price", "oil_id", "type", "show_type", "isxy", "longitude", "latitude", "state"]].fillna('0')
#             data7["create_time"] = sql_time()
#             data7["update_time"] = sql_time()
#             # data7["id"] = '1'
#             print(data7)
#             data7.to_csv("competitor.csv",index=None,encoding="utf-8")
#             print(data7.columns.values)
#             upload_file_monitor()
#         except Exception as e:
#             print("error:合并filling_station表数据和重叠油价表数据:%s"%(e))
#     except Exception as e:
#         print("插入数据不成功:error:%s"%e)
#         pass

def crawl_data():
    #循环执行任务队列
    panzhihua_fz()
    #循环执行异常任务队列
    # panzhihua_fz_error()
    deal_to_sql()
    print("执行123")


#判断队列是否为空
def queue_clear():
    print("===数据爬取前清空队列===")
    global q
    global q_error
    if q.qsize()>0:
        q.queue.clear()
    if q_error.qsize()>0:
        q_error.queue.clear()

def copy_file():
    shutil.copyfile(csv_result_path, data_path)
    shutil.copyfile(csv_result_path, data_city_error_path)
    shutil.copyfile(csv_result_path, data_city_text_path)

#清除弹框xx
def del_tankuang():
    if driver.xpath('//*[@resource-id="com.android.systemui:id/dismiss_view"]').exists:
        driver.click(0.493, 0.874)

if __name__ == "__main__":
    sys.stdout = Logger(log_path)
    # 全局变量，用来存时间
    # dongguan_list = []
    #每间隔一小时跑一次爬虫代码
    while True:
        current_time = datetime.now().time()
        print(current_time)
        # 要在指定时间段内去跑代码
        queue_clear()
        print("当前时间在时间段内")
        delete_file()
        get_files()
        write_spider_title()
        write_spider_title2()
        push_zuobiao()
        # 每次启动前先关闭高德应用程序
        driver.app_stop(package_name='com.autonavi.minimap')
        sleep(1)
        print("-------------------")
        driver.app_start(package_name='com.autonavi.minimap', activity='com.autonavi.map.activity.NewMapActivity')
        if driver(text="本次运行允许").exists:
            print("有弹出框：本次允许运行")
            driver(text="本次运行允许").click()
            print("弹出框点击完毕")
        sleep(1)
        del_tankuang()
        sleep(2)
        delete_tankuang3()
        sleep(2)
        delete_tankuang()
        delete_tankuang2()
        # 升级弹框
        delete_tankuang3()
        sleep(3)
        delete_tankuang8()
        sleep(2)
        delete_qd_tc()
        sleep(1)
        del_tankuang()
        if driver(text="附近").exists:
            driver(text="附近").click()
        else:
            print("附近页面没有加载，等待两分钟重新点击")
            sleep(2)
            driver(text="附近").click()
        sleep(3)
        delete_qd_tc()
        print("程序开始時間:%s" % (datetime.now()))
        print("阿炳真帅气")
        # 攀枝花市-》087乡道东50米
        crawl_data()
        # copy_file()
        # shutil.copy
        # file(csv_result_path, data_path)
        print("当前队列结束,休息5分钟开始下一轮")
        sleep(200)



