
def xy():
    a = 10  # 竞品优惠金额
    c = 0.5  # 易加油比竞品多优惠金额
    y = 0.99  # 后续升数优惠
    p = 5  # 前几升
    n = 7.96  # 挂牌价
    m = 6.96  # 结算价
    w = 3  # 服务费
    t = 0.5  # 额外优惠
    h = 200/n  # 200加油多少升
    # int(h)  # 取整数

    x = y+200*(1-y)/(p*n)-(a+c+w)/(p*n)  # 前p升折扣
    # z = y+(200-200*y-a-c-w)/(p*n)
    d = x*n  # 前p升单价
    dj = (200-a-c+t)*n / 200

    sum1 = p*n*x+(h-p)*n*y+w  # 易加油满两百需付金额
    sum2 = 200-a  # 竞品满两百需付金额

    u = (h*m-t)
    v = 200-a-c


    if(dj < m) :
        print("活动价%s<结算价%s" % (dj, m), "不调价!!")
        print(u,v)
    else:
        print("活动价%s>=结算价%s" % (dj, m), "调价!!")
        print("前%s升%s折,前%s升单价%s元" % (p, x, p, d))
        print("%s+%s=%s" % (sum1, c, sum2))
        print(u, v)

    # print(x,z)
xy()