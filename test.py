def isPrime(N):
        while N<=1000:
                num=0
                j=1
                while j<=N:
                        if N%j==0:
                                num=num+1
                        j=j+1
                if num==2:
                        return 1
                else:
                        return 0
sum=0
for x in range(2,1000):
        if isPrime(x)==1:
                sum=sum+x
        print sum

	
		
	