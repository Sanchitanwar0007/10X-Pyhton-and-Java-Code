for _ in range(int(input())):
    fx1,fy1,fx2,fy2,sx1,sy1,sx2,sy2=map(int,input().split())
    f_len=fx2-fx1
    f_wid=fy2-fy1
    f_area=f_len*f_wid

    s_len=sx2-sx1
    s_wid=sy2-sy1
    s_area=s_len*s_wid

    tota_area=f_area+s_area
    overlap_area=0
    if(sx1>=fx2 or sx2<=fx1 or sy1>=fy2 or sy2<=fy1):
        overlap_area=0

    else:
        f1=min(sx2,fx2)-max(sx1,fx1)
        f2=min(sy2,fy2)-max(sy1,fy1)
        overlap_area=f1*f2
    print(tota_area-overlap_area)
