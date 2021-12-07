# from collections import deque
# def sorted_halfstring(string):  # abdc
#     mid=len(string)//2  # mid=2
#     list=[]
#     for i in range(mid,len(string)):  #[d,c]  #o(n/2)
#         list.append(string[i])
#     for i in range(len(list)):  #len=2 i=0    #(O(n/2*n/2))==>O(n^2)
#         j=i        #j=0
#         while j>0 and list[j]>list[j-1]: #0>0 1>0 # p>i
#             list[j],list[j-1]=list[j-1],list[j]  #
#             j-=1
#     ans=""
#     for i in range(0,mid):
#         ans+=string[i]
#     for i in list:
#         ans+=i
#     return ans
# n=input()
# print(sorted_halfstring(n))


# def fun(n):  # 23
#     count = 0
#     while n != 0:  #4502
#         n //= 10   #23//10-> 2//10==->0  log100==>log(10)^2==>2log10==>log1000==>log454==>
#         count += 1 
#     return count


# def count_moves(chess,row,col,moves):
#     if(row>9 or col>9 or row<0 or col<0):
#         return 0
#     if(moves==0):
#         if(chess[row][col]==0):
#             chess[row][col]=1
#             return 1
#         else:
#             return 0
#     total_moves=0
#     total_moves+=count_moves(chess,row-2,col-1,moves-1)
#     total_moves+=count_moves(chess,row-2,col+1,moves-1)
#     total_moves+=count_moves(chess,row-1,col+2,moves-1)
#     total_moves+=count_moves(chess,row+2,col+1,moves-1)
#     total_moves+=count_moves(chess,row+2,col-1,moves-1)
#     total_moves+=count_moves(chess,row+1,col-2,moves-1)
#     total_moves+=count_moves(chess,row-1,col-2,moves-1)
#     total_moves+=count_moves(chess,row+1,col+2,moves-1)
#     return total_moves
#                             # k+=chess_Play(arr,i-2,j-1,m-1)
#                             # k+=chess_Play(arr,i-2,j+1,m-1)
#                             # k+=chess_Play(arr,i-1,j+2,m-1)
#                             # k+=chess_Play(arr,i+1,j+2,m-1)
#                             # k+=chess_Play(arr,i+2,j+1,m-1)
#                             # k+=chess_Play(arr,i+2,j-1,m-1)
#                             # k+=chess_Play(arr,i+1,j-2,m-1)
#                             # k+=chess_Play(arr,i-1,j-2,m-1)



# row,col,moves=map(int,input().split())  #
# chess=[[0 for i in range(10)] for j in range(10)]
# row=row-1
# col=col-1
# print(count_moves(chess,row,col,moves))


#Left to right rotate

#[2 3 4 5 6]==>L3==>[5 6 2 3 4]
# def rotate_left(arr,k):  #1st: 3 4 5 6 2  2nd: 4 5 6 2 3 3rd: 5 6 2 3 4  4th: 6 2 3 4 5  5th: 2 3 4 5 6  6th:3 4 5 6 2 
#     k=k%len(arr)  #3%5=>3
#     list=[0]*k   
#     for i in range(k):
#         list[i]=arr[i]   #[2,3,4]
#     j=0
#     # print(list)
#     # arr1=[0]*len(arr)  #[0 0 0 0 0]
#     for i in range(k,len(arr)):  # 3 ,4
#         arr[j]=arr[i]  # 0 1  arr1=[5 6]
#         j+=1           # j=2
#         # print(arr[i],end=" ")
#     for i in range(len(list)):  # len(list)==k==3==>0 to 2(inclusive)
#         arr[j]=list[i]  #2 3 arr1[5 6 2 3 4]
#         j+=1  #j=5
#     print(*arr)
# def right_rotation(arr,k): #[2 3 4 5 6]==>[4 5 6 2 3]
#     k=k%len(arr)
#     list=[0]*k
#     j=0
#     for i in range(len(arr)-k,len(arr)):
#         list[j]=arr[i]
#         j+=1
#     # print(list)
#     arr1=[0]*len(arr)
#     for i in range(len(arr)-k):
#         arr1[j]=arr[i]
#         j+=1
#     for i in range(len(list)):
#         arr1[i]=list[i]
        
#     print(*arr1)
# left=0
# rigth=0  
# n,q=map(int,input().split())
# arr=list(map(int,input().split()))
# for i in range(q):
#     r,num=input().split()
#     num=int(num)
#     if(r=='L'):
#         left+=num
#     else:
#         rigth+=num
# if(left>rigth):
#     left=left-rigth
#     # print("left")
#     rotate_left(arr,left)
# else:
#     rigth=rigth-left
#     # print("rigth")
#     right_rotation(arr,rigth)

# # 5 3
# # 1 2 3 4 5
# # L 2
# # R 4
# # L 3
# var sum=0;
# for(int i=1;i<=operationi;i+=1){
#     if(i%k==0){
#         sum+=i
#     }
#     }






# def inversionCount(arr, left, right):
#     count = 0
#     if right > left:
#         mid = (left + right) // 2

#         count += inversionCount(arr, left, mid) # [1, 6, 2, 4, 7] => [1, 2, 4, 6, 7] L[2]

#         count += inversionCount(arr, mid + 1, right) # [3, 5, 10, 8, 9] => [3, 5, 8, 9, 10] R[0]

#         count += merge(arr, left, mid, right)

#     return count


# def merge(arr, left, mid, right):
#     tmp = [0] * (right - left + 1)

#     i = left
#     j = mid + 1
#     k = 0

#     invCount = 0

#     while i <= mid and j <= right:
#         if arr[i] < arr[j]:
#             tmp[k] = arr[i]
#             i += 1
#         else: # L[i] > R[j]
#             tmp[k] = arr[j]
#             invCount += (mid - i + 1)
#             j += 1

#         k += 1

#     while i <= mid:
#         tmp[k] = arr[i]
#         i += 1
#         k += 1

#     while j <= right:
#         tmp[k] = arr[j]
#         j += 1
#         k += 1

#     p = left

#     for x in tmp:
#         arr[p] = x
#         p += 1

#     return invCount

# arr = [2,4,1,3,5]
# print(inversionCount(arr, 0, len(arr) - 1))



# def merge(arr,start,mid,end): # Two Pointer Approach
#     i=start
#     j=mid+1
#     temp_arr=[0]*(end-start+1)
#     idx=0
#     while(i<=mid and j<=end):
#         if(arr[i]<=arr[j]):
#             temp_arr[idx]=arr[i]
#             i+=1
#             idx+=1
#         else:
#             temp_arr[idx]=arr[j]
#             j+=1
#             idx+=1
#     while(i<=mid):
#         temp_arr[idx]=arr[i]
#         i+=1
#         idx+=1
#     while(j<=end):
#         temp_arr[idx]=arr[j]
#         j+=1
#         idx+=1
#     for i in range(start,end+1):
#         arr[i]=temp_arr[i-start]
#     # print(temp_arr)
        


# def mergeSort(arr,start,end):#[1 2 3 4]  [56 7 8 0]
#     if(start<end):
#         mid=(start+end)//2
#         mergeSort(arr,start,mid)
#         mergeSort(arr,mid+1,end)  
#         merge(arr,start,mid,end)

# arr=list(map(int,input().split()))
# mergeSort(arr,0,len(arr)-1)
# print(arr)



#arr1=[4,2,5,6,2,7,3] arr2=[8,2,4,1,5,6,7]

# arr=[2,2,3,4,5,6,7]
# arr2=[1,2,4,5,6,7,8]
# i=0
# j=0
# list=[]
# while(i<len(arr) and j<(len(arr2))):
#     if(arr[i]==arr2[j]):   #2 ==1 i=1 j=2
#         list.append(arr[i])
#         i+=1
#         j+=1
#     elif(arr[i]<arr2[j]):   #2 1 0 0
#         i+=1
#     elif(arr[i]>arr2[j]):  #2 1 0 1
#         j+=1
# print(list)



#aababa ==> ababa aabab
# def merge(arr,start,mid,end):
#     i=start
#     j=mid+1
#     temp=[0]*(end-start+1)
#     k=0
#     in_count=0
#     while(i<=mid and j<=end):
#         if(arr[i]<=arr[j]):
#             temp[k]=arr[i]
#             i+=1
#         else:
#             in_count+=mid-i+1
#             temp[k]=arr[j]
#             j+=1
#         k+=1
#     while(i<=mid):
#         temp[k]=arr[i]
#         i+=1
#         k+=1
#     while(j<=end):
#         temp[k]=arr[j]
#         j+=1
#         k+=1
#     for i in range(start,end+1):
#         arr[i]=temp[i-start]

#     return in_count

# def mergeSort(arr,start,end): #[5,3,2,1] [7,9,0] 
#     count=0
#     if(start<end):
#         mid=(start+end)//2
#         count+= mergeSort(arr,start,mid)  # Ist array
#         count+= mergeSort(arr,mid+1,end)  # 2nd array
#         count+=merge(arr,start,mid,end)
#     return count
# arr=[8,4,2,1]
# ans=mergeSort(arr,0,len(arr)-1)
# print(ans)

# def reverseSelectionSort(A, n):
# 	n=len(A)-1
# 	for i in range(0,n+1):
# 		max1=i
# 		for j in range(i+1,len(A)):
# 			if A[j]>A[max1]:
# 				max1=j
# 		A[i],A[max1]=A[max1],A[i]
# 	return A
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         n = int(input())
#         arr = [int(x) for x in input().split()]
#         print(*reverseSelectionSort(arr, n))


# s="India is great"
# str=""
# arr=s.split(" ")
# for i in range(len(arr)-1):
#     str+=arr[i]+"%20"
# str+=arr[len(arr)-1]
# print(str)

# s=input()
# arr=[0]*256
# for i in range(len(s)):
#     print(ord(s[i]),end=" ")
#     arr[ord(s[i])]+=1

# # print(arr)
# for i in range(len(arr)):
#     if(arr[i]==1):
# #         print(chr(i))

# s=input()
# s2=input()
# if(len(s)<len(s2)):
#     s+=".0"
# else:
#     s2+=".0"
# arr1=s.split(".")
# arr2=s2.split(".")
# i=0
# j=0
# while(i<len(arr1) and j<(len(arr2))):
#     if(arr1[i]==arr2[j]):
#         i+=1
#         j+=1
#     elif(arr1[i]<arr2[j]):
        
# for _ in range(int(input())):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     arr.sort()
#     maxi=max(arr)
#     swr=0
#     last_index=len(arr)-1
#     for i in range(len(arr)):
#         swr+=arr[i]*last_index
#         last_index-=1
#     last_index=len(arr)-1
#     arr.reverse()
#     swithr=0
#     # print(swr)
#     for i in range(len(arr)):
#         swithr+=arr[i]*last_index
#         last_index-=1
#     # print(swithr)
# print(((swithr-swr)*maxi)%1000000007)

# your code goes here
# for _ in range(int(input())):
#     num=int(input())
#     arr=list(map(int,input().split()))
#     set1=set()
#     set2=set()
#     temp_arr=[]
#     for i in arr:
#         temp_arr.append(i)
#     temp_arr.sort()
#     for i in range(len(arr)):
#         if(i%2==0):
#             set1.add(arr[i])
#             set2.add(temp_arr[i])
#     diff=set1-set2

#     print(len(diff))
#     print(set1,set2)

# n=int(input())
# arr=[0]*n
# for i in range(n):
# 	pos,vel=map(int,input().split())
# 	arr[pos]=vel
# vel_arr=[0]*11  #[0 1 2 3 4 5 6 7 8 9 10]
# ans=0
# for i in range(len(arr)):
# 	temp=arr[i]
# 	vel_arr[temp]+=1
# print(vel_arr)
# print(sum(vel_arr))



# 6
# 1 7
# 3 10
# 0 5
# 4 3
# 5 7
# 2 4
# def isSubstring(s1, s2):
#     if s1.find(s2) != -1:
#         return True
#     if s2.find(s1) != -1:
#         return True
#     return False
# def isRotation(s1, s2):
# 	if(len(s1)==0 and len(s2)==0):
# 		print(True)
# 		return True
# 	if(len(s1)<len(s2)):
# 		print(False)
# 	else:
# 		c=s2.find(s1[0])
# 		if(s2.find(s1[0])!=-1):
# 			d=deque(s2)
# 			d.rotate(-c)
# 			t=list(d)
# 			s2=''.join(t)
#             # print(s2)
# 			if(isSubstring(s1,s2)):
# 				print(True)
# 			else:
# 				print(False)
# 		else:
# 			print(False)



# ## You can only call isSubstring function from this function once. Use this function to check if s2 is a rotation of s1.

# ## Do not change anything below
# t = int(input())
# for i in range(t):
#     s1 = input()
#     s2 = input()
#     isRotation(s1, s2)


# for i in range(int(input())):
#     n=int(input())
#     l=list(map(int,input().split()))[:n]
#     c=l.index(min(l))
#     c2=l.index(max(l))
#     c4=0
#     m1=max(l)
#     if(c<c2):
#         pass
#     else:
#         l[c],l[c2]=l[c2],l[c]
#     m=[]

#     c=l.index(min(l))
#     c2=l.index((max(l)))
#     c4=m1-l[l.index(max(l))-1]
#     print(c4)

# n=int(input())
# for i in range(n):
#     s=input()
#     s1=max(s)
#     s=list(s)
#     s.remove(s1)

#     mid=len(s)//2
#     s2=s[:mid]
#     s3=s[mid:]
  
#     s2.sort()
#     s3.sort(reverse=True)
#     s4=''
#     s4=''.join(s2)+s1+''.join(s3)
#     print(s4)


#########Linked list:
# class Node:
#     def __init__(self,data=None,next=None):
#         self.data=data
#         self.next=next  
# def display(head):
#     temp=head
#     while(temp!=None):
#         print(temp.data,end="->")
#         temp=temp.next
# head=Node(12,None)
# # head=new_node
# new_node2=Node(24,None)
# head.next=new_node2
# new_node3=Node(48,None)
# new_node2.next=new_node3
# new_node4=Node(96,None)
# new_node3.next=new_node4

# display(head)


# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None


# class LinkedList:

#     def __init__(self):
#         self.head = None

#     def push(self, new_value):
#         new_node = Node(new_value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
#         self.tail.next = new_node
#         self.tail = new_node

#     def isPalin(self):

#         return self.checker()

#     def reverse(self):
#         prev = None
#         current = self.head
#         while (current is not None):
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#         return prev
#     def checker(self):
#         temp=self.head
#         t=temp
#         while(t!=None):
#             print(t.data,end=" ")
#             t=t.next
        
#         temp1 =self.reverse()
#         print()
#         t2=temp1
#         while(t2!=None):
#             print(t2.data,end=" ")
#             t2=t2.next
#         print()
#         f=1
#         while(temp!=None):
#             print(temp.data)
#             print(temp1.data)
#             # if(temp.data!=temp1.data):
#             #     f=0
#             temp = temp.next
#             temp1 = temp1.next
#         if(f==0):
#             return False
#         else:
#             return True
# def read_list_input():
#     vals = input().split(' ')
#     linkedList = LinkedList()
#     for val in vals:
#         linkedList.push(val)
#     return linkedList


# test_cases = int(input())
# for i in range(test_cases):
#     linkedList = read_list_input()
#     print(linkedList.isPalin())


# class Node:
#     def __init__(self,data):  #Parametrized Constructor of class Node
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None

#     def append(self,val):
#         new_Node=Node(val)
#         if(self.head==None):
#             self.head=new_Node
#             self.tail=self.head
#             return
#         self.tail.next=new_Node
#         self.tail=new_Node
#     def display(self):
#         temp=self.head
#         while(temp!=None):
#             print(temp.data,end="->")
#             temp=temp.next
#         print(None)
#     def insertAtHead(self,data):
#         new_node=Node(data)
#         if(self.head==None):
#             self.head=new_node
#             return
#         new_node.next=self.head
#         self.head=new_node


# l=LinkedList()
# l.append(20)
# l.append(21)
# l.append(22)
# l.append(23)
# l.append(50)
# l.display()
# l.insertAtHead(11)
# l.display()


# class Node: 
#     def __init__(self, value): 
#         self.data = value 
#         self.next = None
        
# class LinkedList: 
  
#     def __init__(self): 
#         self.head = None
  
#     def push(self, new_value): 
#         new_node = Node(new_value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
#         self.tail.next = new_node
#         self.tail = new_node 
#     def reverse(self,node):
#         prev=None
#         curr=node.next
#         while(curr!=None):
#             temp=curr.next
#             curr.next=prev
#             prev=curr
#             curr=temp
#         node.next=prev
#     def isPalin(self):
#         slow=self.head
#         fast=self.head.next
#         while(fast!=None and fast.next!=None):
#             slow=slow.next
#             fast=fast.next.next
#         self.reverse(slow)
#         temp=self.head
#         while(temp!=None):
#             print(temp.data,end="->")
#             temp=temp.next

# def read_list_input():
#     vals = input().split(' ')
#     linkedList = LinkedList() 
#     for val in vals:
#         linkedList.push(val)
#     return linkedList

# test_cases = int(input())
# for i in range(test_cases):
#     linkedList = read_list_input()
#     print(linkedList.isPalin())

# def f(n, i=1):
#     if (n>=5):
#         return n
#     n = n + i
#     i = i + 1
#     return f(n,i)
# print(f(1))
# print(2 * 3 ** 3 * 4)

# t=int(input())
# z=[int(x) for x in input().split()]

# l=[str(x) for x in z]
# l=sorted(l,key=lambda z : z.count('2'),reverse=True)
# for i in range(1,t):
#     if l[i].count('2')==l[i-1].count('2'):
#         if int(l[i])>int(l[i-1]):
#             l[i],l[i-1]=l[i-1],l[i]
# for i in l:
#     print(int(i),end=" ")
# function two_dimension(arr){
# 	for(var i=0;i<arr.length;i++){
# 		var str="";
# 		if(i%2==0){
# 			for(var j=0;j<arr[0].length;j++){
# 				str+=arr[i][j]+" ";
# 			}
# 		}else{
# 			for(var j=arr[0].length-1;j>=0;j--){
# 				str+=arr[i][j]+" ";
# 			}
# 		}
# 		console.log(str);
# 	}
# }
# arr=[[1,2,3],
# 	 [4,5,6],
# 	 [7,8,9],
# 	 [10,11,12]]
# two_dimension(arr)


# a,k=map(int,input().split())
# arr=list(map(int,input().split()))
# cum_sum=[]
# sum=0
# if a==0:
#     print(0)
# else:
#     for i in range(len(arr)):
#         sum+=arr[i]
#         cum_sum.append(sum)
#     x=cum_sum.count(k)
#     if x<=0:
#         print(0)
#     else:
#         first_occ=0
#         occrence=[]
#         c=1
#         for i in range(len(cum_sum)):
#             if cum_sum[i]==k:
#                 first_occ=c
#                 occrence.append(first_occ)
#             c+=1
#         print(max(occrence))

# def gcd(a,b):
#     if(a==0):
#         return b
#     if(b==0):
#         return a
#     if(a>b):
#         return gcd(a-b,b)
#     return gcd(a,b-a)
# ans=gcd(0,0)
# print(ans)

# def calSumUtil( A , B , n , m ): # n >= m

#     add_arr =[]
#     carry = 0

#     i = n-1
#     j = m-1

#     carry = 0
#     while i>=0 and j >= 0:
#         temp = A[i] + B[j] + carry
#         carry = temp // 10
#         temp = temp%10
#         add_arr.append(temp)
#         i -= 1
#         j -= 1
    
#     while i>= 0:
#         temp = A[i] + carry
#         carry = temp//10
#         temp = temp%10
#         add_arr.append(temp)
#         i-=1
#     if carry > 0:
#         add_arr.append(carry)

#     return add_arr[::-1]
# # Wrapper Function 
# def calSum(a, b, n, m ): 
  
#     # Making first array which have 
#     # greater number of element
#     # A is the first array
#     # n is size of array A
#     # B is the second array
#     # m is size of array B 
#     if n >= m: 
#         return calSumUtil(a, b, n, m) 
#     else: 
#         return calSumUtil(b, a, m, n) 
  
# # Driven Code 
# testCase = int(input())
# for _ in range(testCase):
# 	A = list(map(int,input().split()))
# 	B = list(map(int,input().split()))
# 	res = calSum(A, B, len(A), len(B))
# 	print(*res)


# import math
# def is_prime(n):
#     if n <= 1:
#         return False

#     max_div = math.floor(math.sqrt(n))
#     for i in range(2, 1 + max_div):
#         if n % i == 0:
#             return False
#     return True


# def totalnumberofprimenumber(arr, n, K):

#     start = 0
#     end = n - 1


#     while start <= end:

#         mid = (start + end) // 2

#         if arr [ mid ] == K:
#             return mid+1

#         elif arr [ mid ] < K:
#             start = mid + 1
#         else:
#             end = mid - 1


#     return end + 1

# q,m=map(int,input().split())

# l=[]
# for n in range(1,q):
#     x = is_prime(n)
#     if(x==True):
#         l.append(n)
# # print(l)
# for i in range(m):
#     c=int(input())
#     count=totalnumberofprimenumber(l,len(l),c)
#     print(count)

# def Target_sum(arr, n , k , i):
#     if k==0:
#         return 1
#     if i==n or k<0:
#         return 0
#     return Target_sum(arr, n ,k-arr[i],i) + Target_sum(arr, n ,k , i+1)
# m , n = map(int, input().split())
# arr = list(map(int, input().split()))
# print(Target_sum(arr, len(arr), n, 0))

# s=input()
# l=[]
# maxi=0
# for i in s:
#     if i in l:
#         l=l[l.index(i)+1:]
       
#         l.append(i)
#     else:
#         l.append(i)
#         if(len(l)>maxi):
#             maxi=len(l)

# print(maxi)

# myString="IYER has played well"

# count=0

# for i in range(len(myString)):

#     if myString[i]==" ":

#         continue

#     elif (ord("a")-ord(myString[i]))>0:

#         count=count+1
# print(count)


# myString="My name is JamesBond"

# myString=myString.capitalize()

# myString=myString.replace("J","s")
# print(myString)

# m=int(input())
# n=int(input())

# for k in range(n*n):

#     i=k/n
#     j=k%n

# your code goes here
# a=int(input())
# b=int(input())
# print(a//b)
# print(a%b)
# print(f"({a//b} {a%b})")
# print("c:"'//'"doc")
# def recurse(string,i,j,val):
#     if j>=len(string):
#         return val
#     if string[j]==string[i]:
#         val+=1
#     return recurse(string,i,j+1,val)
# myString="Jadeja"
# sum=0
# for i in range(len(myString)-1):
#     sum=sum+recurse(myString,i,i+1,0)
# print(sum)
# arr=[17,12,15,10,21,9,15]
# i=0
# j=len(arr)-1
# while(arr[i]>arr[j]):
#     i+=1
#     j-=1
# # print(i,j)
# myString="India has won against Pakistan"

# myString=myString.capitalize()

# myString=myString.replace("P","s")
# print(myString)
# D = dict()

# for x in enumerate(range(2)):

#     D[x[0]] = x[1]

#     D[x[1]+7] = x[0]

# print(D)

# resList = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]

# print(resList)

# a =[4,3,2,1,0]
# n = len(a)

# j = 0

# for i in range(n):

#     while j < n and a[i] < a[j]:
        
#         j += 1
#         if(i==1):
#             print(j)

# def count(a,val):
    

#     right = len(a)-1

#     left=0

#     while(right>=left):

#         mid=(left+right)//2

#         if a[mid]==val:

#             leftindex=mid-1

#             count=0

#             while(leftindex>=0 and a[leftindex]==val):

#                 leftindex-=1

#             rightindex=mid+1

#             while(rightindex<=len(a)-1 and a[rightindex]==val):

#                 rightindex+=1

#             return [rightindex-1,leftindex+1]

#         elif a[mid]>val:

#             left=mid+1

#         else:

#             right=mid-1
#         print(left,right)
# a =[14,10,9,9,9,5,5,5,1,1]

# right = len(a)-1

# left=0

# a=count(a,5)
# print(left,right)
 

# def func2(ans,n):
#     print("yes")
#     return "Success"

# def func1(arr,n,ans):

#     if arr[n] in ans:

#         return func2(ans,n)

#     ans.append(arr[n])

#     return func1(arr,n+1,ans)

# strings=["manas","sunny","shan","manas","shan"]

# func1(strings,0,[])

# dictionary1 = {'Google' : 1, 

#             'Facebook' : 2, 

#             'Microsoft' : 3

#             } 

# dictionary2 = {'GFG' : 1, 

#             'Microsoft' : 2, 

#             'Youtube' : 3

#             } 

# dictionary1.update(dictionary2); 

# for key, values in dictionary1.items(): 

#     print(key, values , end=" ")


m=[0]
def func(arr,n,k,c,s,arr_len) :
    if(n<k):
        return
    if(c==n):
        if(s==k and arr_len==k):
            m[0]=1
        return
    if(m[0]!=1):
        func(arr,n,k,c+1,s+arr[c],arr_len+1)
        func(arr,n,k,c+1,s,arr_len)
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
func(arr,len(arr),k,0,0,0)
if(m[0]==1):
    print(True)
else:
    print(False)

