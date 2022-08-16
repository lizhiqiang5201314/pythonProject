
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
    i = 0.8  # 第一梯度，全量升数按价差空间抽佣比例
    f = 0.8  # 第二梯度，后续升数按价差空间抽佣比例
    p1 = 1
    w1 = 1  # 第一阶段服务费

    danjia = (200-a-c+t)*n / 200  # 调价后单价

    x1 = y1 = (n-k*(1-i))/n

    y = (n-k*(1-f))/n  # 后续升数基于对比价y折

    x = ((200-a-c)-z*y*(h-p)-w)/(z*p)  # 前 p升基于对比价 x折

    sum = h*m-t
    sum1 = z*y1*h+w1
    sum2 = z*x*p+z*y*(h-p)+w

    if m > danjia:
        print('不调价！单价%s<结算价%s' % (danjia, m))

    else:
        print('调价！单价%s>结算价%s' % (danjia, m))
        print('加油最低总金额%s,竞品加油总金额%s' % (sum, 200 - a))
        print('一梯度加油总金额%s,全量升数%s折' % (sum1, y*10))
        print('二梯度加油总金额%s,前%s升%s折,后%s升%s折' % (sum2, p, x*10, int(h-p), y*10))


if __name__ == '__main__':
    xy_xy1()