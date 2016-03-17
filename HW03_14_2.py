# -*-coding: utf-8 -*-
x=input('請輸入一數字:')
while x<=200:
	num=0
	j=1
	while j<=x:
		if x%j==0:
			num=num+1
		j=j+1
	if num==2:
		print '%d為質數' %x
	else:
		print '%d不是質數' %x
	break