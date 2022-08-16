
def xy_xy1():
    g = 9.5  # 国家价g元/升
    n = 8.0  # 挂牌价n元/升
    m = 7.5  # 结算价m元/升
    v = 7.6  # 当前用户价v元/升
    p = 10  # 前10升
    z = n  # 活动对比价
    a = 10  # 竞品满200元优惠a元
    c = 0.5  # 易加油比竞品多优惠c元
    w = 3  # 服务费w元
    t = 0  # 满200元可额外补贴t元
    h = 200/n  # 200元加油升数h=200/n
    k = n-m  # 价差空间
    f = 0.8  # 后续升数按价差空间抽佣比例
    w1 = 1  # 第一阶段服务费

    danjia = (200-a-c+t)*n / 200  # 调价后单价

    y = (n-k*(1-f))/n  # 后续升数基于对比价y折

    x = ((200-a-c)-z*y*(h-p)-w)/(z*p)  # 前 p升基于对比价 x折

    sum1 = z*y*h+w1
    sum2 = z*x*p+z*y*(h-p)+w

    print(sum1)
    print(sum2)



    print(x, y)
    if m > danjia:
        print('不调价！单价%s<结算价%s' % (danjia, m))

    else:
        print('调价！')


if __name__ == '__main__':
    xy_xy1()