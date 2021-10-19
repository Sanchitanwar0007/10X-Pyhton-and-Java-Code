def maxWaterTrap(array):
    maxRight=[0]*len(array)
    maxLeft=[0]*len(array)
    max=array[0]
    for i in range(len(array)):
        if(array[i]>max):
            maxLeft[i]=array[i]
            max=array[i]
        else:
            maxLeft[i]=max
    maxR=array[len(array)-1]
    for i in range(len(array)-1,-1,-1):
        if(array[i]>maxR):
            maxRight[i]=array[i]
            maxR=array[i]
        else:
            maxRight[i]=maxR
    maxWaterTrap=0
    print(maxLeft,maxRight)
    for i in range(len(array)):
        maxWaterTrap+=min(maxLeft[i],maxRight[i])-array[i]
    print(maxWaterTrap)
arr=[5,1,2,0,0,4,2,3]
maxWaterTrap(arr)