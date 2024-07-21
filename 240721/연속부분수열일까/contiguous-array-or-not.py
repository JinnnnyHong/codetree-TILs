def is_subsequence(A, B):
    n1 = len(A)
    n2 = len(B)
    
    if n2 > n1:
        return False
    
    
    for i in range(n1 - n2 + 1):
        if A[i:i + n2] == B:
            return True
    
    return False


a, b = map(int, input().split())  
lst1 = list(map(int, input().split()))  
lst2 = list(map(int, input().split()))  


if is_subsequence(lst1, lst2):
    print("Yes")
else:
    print("No")