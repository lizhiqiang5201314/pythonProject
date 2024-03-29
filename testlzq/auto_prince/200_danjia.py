def xy_danjia():
    g = 8.5  # 国家价 g 元/升
    n = 8.0  # 挂牌价  n 元/升
    m = 7.3  # 结算价 m 元/升
    v = 7.6  # 当前用户价 v 元/升
    a = 13  # 竞品满200元优惠a元
    c = 0.5  # 易加油比竞品多优惠c元
    w = 3  # 服务费w元
    u = 0  # 最高额外补贴u元/升
    h = 200/n  # 200元加油升数h = 200/n

    dj = (200-a-c)*n/200+u  # 计算得出的单价

    x = v-n+(a+c+w)*n/200  # 基于当前用户单价补贴X元/升

    y = v-m+u  # 最高补贴Y元/升

    sum1 = (v-x)*h+w  # 补贴x元/升时总价

    sum = 200-a  # 竞品加油总金额

    if m > dj:   # 单价低于结算价
        print('单价%s<结算价%s不调价！' % (dj, m))

    else:  # 单价低于结算价
        if x > y:

            print('不调价！')
            print('基于当前用户单价补贴%s>最%s高补贴' % (x, y))
        else:

            print('调价！')
            print('调价后单价%s>=%s' % (dj, m))
            print('基于当前用户单价补贴%s/升' % x)
            print('易加油加油总价%s+%s=竞品加油总价%s' % (sum1, c, sum))



if __name__ == '__main__':
    xy_danjia()