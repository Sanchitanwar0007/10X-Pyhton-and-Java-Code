def binomialCoeff(n, r):
    # Implement this function
    if(r>n):
        return 0
    if(r==0 or r==n):
        return 1
    return binomialCoeff(n-1,r-1)+binomialCoeff(n-1,r)
# Do not edit anything below
if __name__ == "__main__":
    numTcs = int(input())
    for index in range(numTcs):
        inputInts = input().split(' ')
        n = int(inputInts[0])
        r = int(inputInts[1])
        print(binomialCoeff(n, r))



# def binomialCoeff(n, k):
#     if k > n:
#         return 0
#     if k == 0 or k == n:
#         return 1
 
#     # Recursive Call
#     return binomialCoeff(n-1, k-1) + binomialCoeff(n-1, k)
# if __name__ == "__main__":
#     numTcs = int(input())
#     for index in range(numTcs):
#         inputInts = input().split(' ')
#         n = int(inputInts[0])
#         r = int(inputInts[1])
#         print(binomialCoeff(n, r))