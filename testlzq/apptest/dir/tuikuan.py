from time import sleep
import requests
from selenium import webdriver

# 定义变量
global Id, orderId, username, password, urlhead


# 订单号
orderId = 9110000020188758



inputurl = input("测试：dev  预发布环境：pre  灰度环境:grey  生产环境:www \n请输入退款环境：")
if inputurl == 'dev':
    username = '二十五日'  # 测试环境
    password = '123456'   # 测试环境
    urlhead = 'dev'

elif inputurl == 'pre':
    username = '二八加油站'  # pre环境
    password = '123456'   # pre环境
    urlhead = 'pre'

elif inputurl == 'grey':
    username = '海洋石油石津加油站'  # 灰度环境
    password = '147258369'         # 灰度环境
    urlhead = 'grey'

elif inputurl == 'www':
    username = '海洋石油石津加油站'  # 生产环境
    password = '147258369'         # 生产环境
    urlhead = 'www'

else:
    print('输入有误，清重新输入')

def getcookie():
    driver = webdriver.Chrome()  # 初始化chrome浏览器
    driver.minimize_window()
    driver.get("http://" + urlhead + ".ejiayou.com/station_platform/view/viewLogout.ac?loginType=1000")  # 浏览器打开页面
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_xpath('//*[@id="loginform"]/div[4]/button').click()
    sleep(2)
    global cookie
    cookies = driver.get_cookies()
    if inputurl == 'www':
        cookie = cookies[1]['value']  # 生产环境
    else:
        cookie = cookies[0]['value']  # 测试环境
    # print(cookie)
    # print(cookies)


# 登入收银系统
def login():
    url = 'http://' + urlhead + '.ejiayou.com/station_platform/pc/isfirst.ac'
    data = {
            "username": username,
            "password": password
            }
    r = requests.post(url, data=data)
    if r.status_code == 200:
        print('登陆成功')
    else:
        print('登录失败')


# 退款申请
def setorder():
    url = 'http://' + urlhead + '.ejiayou.com/oreo/openapi/createRefundApplyForWx/v1/13136064545'
    data = {
        "orderId": orderId,
        "reason": "测试人员退款"
        }
    r = requests.post(url, json=data)
    if r.json()['msg'] == 'SUCCESS':
        print('申请成功')
    else:
        print('申请失败')


# 退款同意
def backorder():
    url = "http://" + urlhead + ".ejiayou.com/station_platform/pc/applyRefundv2.ac"
    headers = {
        "cookie": 'SESSION=' + cookie
              }
    data = {
        "orderId": orderId,
        "refundType": "0"
    }
    r = requests.post(url, headers=headers, data=data)

    print(r.json()['msg'])


if __name__ == "__main__":
    getcookie()
    login()
    setorder()
    backorder()