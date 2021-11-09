def groupAnagrams(s):
    d={}
    for i in s:
        k=''.join(sorted(i))
        if( k not in d):
            d[k]=[i]
        else:
            d[k].append(i)
    l=[]
    for i in list(d.values()):
        i.sort()
        l.append(i)
    if(len(l)==0):
    	l.append([''])
    	return l
    else:
    	return l
    

if __name__ == '__main__':

    for _ in range(int(input())):
        n = int(input())
        arr = input().split()

        print(groupAnagrams(arr))