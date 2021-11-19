class bank:
    data1=0
    def __init__(self,data):
        self.data=data
        
    def credit(self,ans):
        ans+=self.data
        return ans
    def debit(self,ans):
        ans+=self.data
        return ans
    
           
        
if __name__ == '__main__':
    n=int(input())
    ans=0
    for i in range(n):
        num=int(input())
        balance=bank(num)
        if(num>0):
            ans=balance.credit(ans)
        else:
            ans=balance.debit(ans)
    print(ans)
    
    
    