#Given an array of integers, return the highest product possible by multiplying 3 numbers from the array

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        l = [None]*3
        t = []
        q = []
        product = A[0]*A[1]*A[2]
        if A[1] > A[0]:
            l[1] = A[0]
            l[0] = A[1]
        else:
            l[1] = A[1]
            l[0] = A[0]
            
        if A[2] > l[0]:
            l[2] = l[1]
            l[1] = l[0]
            l[0] = A[2]
        elif A[2] > l[1]:
            l[2] = l[1]
            l[1] = A[2]
        else:
            l[2] = A[2]
        
        for i in range (3,len(A)):
            if A[i] > l[0]:
                l[2] = l[1]
                l[1] = l[0]
                l[0] = A[i]
            elif A[i] > l[1]:
                l[2] = l[1]
                l[1] = A[i]
            elif A[i] > l[2]:
                l[2] = A[i]
                
        for i in range (len(A)):
            if A[i] < 0:
                q.append(A[i])

        if len(q)>1:
            if q[0] < q[1]:
                t.append(q[0])
                t.append(q[1])
            else:
                t.append(q[1])
                t.append(q[0])
            for i in range (2,len(q)):
                if q[i] < t[0]:
                    t[1] = t[0]
                    t[0] = q[i]
                elif q[i] < t[1]:
                    t[1] = q[i]
        if l[2]:
            product = l[0]*l[1]*l[2]
        if len(l) != 0 and len(t)>1:
            if l[0]*t[0]*t[1] > product:
                product = l[0]*t[0]*t[1]
        return product
        
        
        
        
        
        
        
        
        
        
        
        
        
