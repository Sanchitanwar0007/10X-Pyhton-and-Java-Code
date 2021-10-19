def game(m,k):
    if(m==1):
       return 1
    else:
       return (game(m-1,k)+k-1)%m+1   #josephus(n, k) = (josephus(n - 1, k) + k-1) % n + 1


n=int(input())
for i in range(n):
    m,k=map(int,input().split())
    print(game(m,k))