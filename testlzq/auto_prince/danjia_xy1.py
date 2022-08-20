def danjia_xy1():
    g = 8.5  # 国家价g元/升
    n = 8.0  # 挂牌价n元/升
    m = 7.2  # 结算价m元/升
    v = 7.4  # 当前用户价v元/升
    r = 0.01  # 比竞品优惠金额
    z = n  # 活动对比价z元/升
    t = 1  # 加油满h升可额外补贴 t 元
    h = 25  # 参与活动升数
    k = n-m  # 价差空间k=n-m 元/升
    f = 0.8  # 后续升数按价差空间抽佣比例f
    e = 7.0  # 竞品单价e元/升
    p = 10  # 前p升

    x1 = (e-r)/z  # 前 p升基于对比价 x折

    y = (n-k*(1-f))/n  # 后续升数基于对比价 y 折计算

    danjia = (m*h-t-z*y*(h-p))/p+r  # 调价后单价

    x2 = (v*h-z*((n-k*(1-f))/n)*(h-p))/(z*p)

    x = min(x1, x2)

    if e < danjia:
        print('不调价！')
        print('调价！,单价%s>竞品单价%s' % (danjia, e))

    else:
        print('调价！,单价%s<=竞品单价%s' % (danjia, e))
        print('前面升数%s折,后续升数%s折' % (x*10, y*10))
        print('满足用户加油h升透出单价：%s<竞品单价%s' % (z*x, e))


if __name__ == '__main__':
    danjia_xy1()