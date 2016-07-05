__author__ = 'daijielei'



#等额本息月供计算，P=贷款总额，nlx=年利率，month=贷款月数     【返回值】A=月供
def debx_calac(P=220500,nlx=0.0605,month=36):
    i = nlx/12  #公式里用的为月利率，年利率需要换算为月利率
    n = month
    A = P*(i*((1+i)**n)/(((1+i)**n)-1))     #等额本息月供计算公式
    return A


#计算贷款的实际利率（已知月供），P=贷款总额，A=月供，month=贷款月数，【返回值】i=实际利率
def debx_calac_lx(P=220500,A=6713,month=36):
    i = 0
    while i < 100:#根据假设利率计算月供和实际月供进行比较，找到实际利率
        i = i + 0.0001
        rA = debx_calac(P,i,month)#用假设利率计算月供
        if(int(rA) == int(A)):
            print(rA,A,i)
            return i


#回报计算，用来计算每月需要付出月供的情况下的总回报和每月回报 P=贷款总额，hbl=预期回报率（年），payback=每月支付月供金额     ，【返回值：】allreback=总收益，monthback=每月收益
def huibaojisuan(P=220500,hbl=0.05,payback = 6713):
    allreback = 0
    i = hbl/12
    monthback = []

    while P > 0:
        sy = P*i    #计算当月收益
        allreback = allreback + sy  #总收益

        #P = P - payback + sy       #如果收益能够滚动成本金进行再投资，可以明显降低一些对回报率的需要
        P = P - payback     #下月可投资本金扣除当月月供

        if P > 0:
            monthback.append((float('%.2f'%P),float('%.2f'%(sy))))
        else:
            monthback.append((0,float('%.2f'%(sy))))

    return allreback,monthback


#需要多少利率能抵消利息即手续费开销，P=贷款总额，sxf=手续费（或其他一次性成本），nlx=年利率，month=贷款月数  ，【返回值】i=能覆盖成本的回报率
def howmanyRetrunCanbeenough(P=220500,sxf=6615,nlx=0.0605,month=36):
    ykk = debx_calac(P,nlx,month)#计算月供
    allCostmoney = sxf + (ykk-P/month)*month   #计算手续费和全部利息开销之和
    print('allCostmoney {}:'.format(allCostmoney))

    i = 0
    while i < 100:  #循环寻找最小能覆盖成本的投资收益率
        i = i + 0.001
        hbe,alb = huibaojisuan(P,i,ykk)
        if(hbe>allCostmoney):   #将总成本和回报进行比较
            print(i)
            return i




if __name__ == '__main__':
    debx_calac_lx()
    howmanyRetrunCanbeenough()
