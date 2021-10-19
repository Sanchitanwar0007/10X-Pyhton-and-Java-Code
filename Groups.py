def groupAnagrams(strs):
    arr=[]
    map={}
    for i in range(len(strs)):
        a=sorted(strs[i])
        temp="".join(a)
        arr.append((temp,i))
    arr.sort(key=lambda x:x[0])
    print(arr)
    temp=[]
    ans=[]
    for i in range(len(arr)-1):
        if(arr[i][0]==arr[i+1][0]):
            print(strs[arr[i][1]])
            temp.append(strs[arr[i][1]])


    

if __name__ == '__main__':

    for _ in range(int(input())):
        n = int(input())
        arr = input().split()

        print(groupAnagrams(arr))