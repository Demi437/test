# -*- coding: utf-8 -*-
money=input('How much do you want to draw?')
save=5000
deposit=save-money
if deposit>0:
	print '您的存款還剩%d多少元' %deposit
elif deposit==0:
	print '您的存款無剩餘存款'
else:
	print '您的存款不足!'
f=open("result.txt","a")
f.write("您還有存款%d元" %(deposit))
f.close()
