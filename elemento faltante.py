

from copy import copy


def solution (A):
    B=[]
    for c in range (0, len(A)):
        l=int (A[c])
        B.append(l)
    B.append(0)
    print (B)
    print (A)

    for a in range (0, len(A)):
        #print ("A[a]-1: "+ str ((A[a])-1))
        temp1 = (A[a])-1
        print (temp1)
        temp2 = A[a] 
        print (temp2)
        B[temp1]= temp2
    print (B)
    for a in range (0, len(B)-1):
        if B[a+1]!=B[a]+1:
            elemento=B[a]+1
            break
        else:
            elemento=0
    return elemento

print (solution ([2,3,1,5]))