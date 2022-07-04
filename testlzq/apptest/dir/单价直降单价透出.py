
def danjia():
    n = 8.0  # 挂牌价
    m = 7.2  # 结算价
    v = 7.6  # 当前用户价
    r = 0.01 #  易加油比竞品低
    t = 0   # 最高补贴t元/升
    s = 0.1  # 最高抽佣s元/升
    e = 7.6  # 竞品单价
    y = 0-s


    dj = m+r-t
    i = v-e+r
    q = e-r

    if(dj>e) :
        print("不调价！")
    else:
        print("调价！")
        if(i<y) :
            x1=i
        else:
            x2=y

    print(x2)



danjia()