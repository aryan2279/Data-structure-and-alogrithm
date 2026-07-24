class Solution:
    def fwht(self,a,inv):
        n=len(a)
        length=1

        while length<n:
            for i in range(0,n,length<<1):
                for j in range(length):
                    u=a[i+j]
                    v=a[i+j+length]
                    a[i+j]=u+v
                    a[i+j+length]=u-v
            length<<=1

        if inv:
            for i in range(n):
                a[i]//=n

    def uniqueXorTriplets(self, nums):
        N=2048
        f=[0]*N

        for x in nums:
            f[x]=1

        self.fwht(f,False)

        for i in range(N):
            f[i]=f[i]*f[i]*f[i]

        self.fwht(f,True)

        ans=0
        for x in f:
            if x!=0:
                ans+=1

        return ans