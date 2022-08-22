
def mydanjia():
    n = 8.0  # 挂牌价
    m = 7.5  # 结算价
    v = 7.6  # 当前用户价
    k = n-m  # 价差
    f = 0.8  # 按价差抽拥比例

    x = v-n+k*(1-f)


    if k > 0:
        print('调价！,价差空间%s>0' % k)
        if x > 0:
            print('补贴：%s，用户单价%s<%s' % (x, v-x, n))
        else:
            print('抽拥：%s，用户单价%s<%s' % (-x, v-x, n))

    else:
        print('不调价，价差空间%s<0' % k)

if __name__ == '__main__':
    mydanjia()
