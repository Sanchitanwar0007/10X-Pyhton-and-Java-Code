def intersect(nums1, nums2):
    # implement this function
    i=0
    j=0
    ans=[]
    while(i<len(nums1) and j<len(nums2)):
        if(nums1[i]==nums2[j]):
            ans.append(nums1[i])
            i+=1
            j+=1
        elif(nums1[i]<nums2[j]):
            i+=1
        elif(nums1[i]>nums2[j]):
            j+=1
    if(len(ans)>0):
        return ans
    else:
        return [-1]

# DO NOT change anything below this line
if __name__ == "__main__":
    num1_len = int(input())
    nums1 = []
    for index in range(num1_len):
        nums1.append(int(input()))
    num2_len = int(input())
    nums2 = []
    for index in range(num2_len):
        nums2.append(int(input()))

    for element in intersect(nums1, nums2):
        print(element)