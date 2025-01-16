#RESULT
t = int(input())

for i in range(t):
    n = int(input())
    mats = list(map(int, input().split()))
    art = list(map(int, input().split()))

    # YES NO YES
    # [1, -1, -1, -1] 
    # [1, 1, -2]
    # [2, -7]
    #RUNTIME COMPLEXITY: O(4N)
    tot = 0
    res = "YES"
    difference = []
    exc = [0] * n
    for idx in range(len(mats)):
        difference.append(art[idx]-mats[idx])
    for num in range(len(difference)):
        val = max(0, difference[num])
        if val != 0:
            exc[num] = val
        tot += val
    for num in range(len(difference)):
        difference[num] += (tot - 2*exc[num])
    for num in difference:
        if num > 0:
            res = "NO"
            break
    print(res)
        
        
