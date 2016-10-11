# -*- coding:utf-8 -*-

u'''
数值积分 - 矩形法
'''
def djf(a,b,f,delta):
	u'''
	矩形法
	参数依次为积分下限、积分上限、被积函数、精度（delta x）
	'''
	x = a
	s = 0
	while x<=b:
		x = x + delta
		s = s + f(x)
	return s*delta

for delta in [0.1,0.01,0.001,0.0001,0.00001,0.000001]:
	print u"函数f(x)=x从0到10积分，\t\t精度为%f时近似值："%delta,djf(0,10,lambda x: x,delta)
for delta in [0.1,0.01,0.001,0.0001,0.00001,0.000001]:
	print u"函数f(x)=x^2从0到10积分，\t精度为%f时近似值："%delta,djf(0,10,lambda x: x**2,delta)
