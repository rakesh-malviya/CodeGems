def lis_itr_n2(A):
    n = len(A)
    dp = [1 for _ in range(n)]

    for i in range(1,n):
        for j in range(i):
            if A[i] > A[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j]+1

    return max(dp)

def bisect_left1(A,k):
    low  = 0
    high = len(A) - 1
    while(low <= high):
        mid = int(low + (high - low) / 2)
        if k < A[mid]:
            high = mid - 1

        elif k > A[mid]:
            low = mid+1
        else:
            return mid

    if k > A[mid]:
        return mid+1
    else:
        return mid


def lis_nlogn(A):
    dp = []
    dp.append(A[0])
    for i in range(1,len(A)):
        index = bisect_left1(dp,A[i])
        if index >= len(dp):
            dp.append(A[i])
        else:
            dp[index] = A[i]

    return len(dp)

import random

while True:
    n = 10
    A = [random.randint(0,100) for _ in range(n)]
    r1 = (lis_itr_n2(A))
    r2 = (lis_nlogn(A))
    print(r1,r2)
    assert r1 == r2

