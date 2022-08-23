def myxy1():
    g = 8.5  # 国家价g元 / 升
    n = 8.0  # 挂牌价n元 / 升
    m = 7.5  # 结算价m元 / 升
    v = 7.6  # 当前用户价v  元 / 升
    z = n  # 活动对比价z元 / 升
    t = 1  # 用户加油满200元 ，盈利
    h = 200/n  # 200元加油升数
    k = n-m  # 价差空间
    f = 0.8  # 后续升数按价差空间抽佣比例
    p = 10  #


    y = (n-k*(1-f))/n  # 后续升数折扣

    x = (m*h+t-z*y*(h-p))/(z*p)  # 前p升折扣

    sum1 = m*h + t  # 200元应付金额

    sum2 = z*x*p+z*y*(h-p)  # 200元应付金额

    if sum1 == sum2:
        print('调价！')
        print('前%s升%s折，后续升数%s折' % (p, x*10, y*10))
        print('200元加油金额%s=%s' % (sum1, sum2))

    else:
        print('不调价！')
        print('200元加油金额' % (sum1, sum2))


if __name__ == '__main__':
    myxy1()
