"""
Pair  Having Similar Elements

Given an array A , having N integers A1, A2, A3....An.
Two elements of an array are called similar if Ai = Aj + 1
or Aj = Ai + 1 , Also similarity follows transitivity.
if Ai and Aj are similar and Aj and Ak are similar, then
Ai and Ak are also similar.

Note i,j,k are all distinct

You need to find the number of pairs of indices i,j
such that i<j and Ai is similar to Aj

Input 
------
First line contains a single integer N denoting
number of elements in the array 
The Second line contains N space seperated integers
where ith elements indicate Ai

Output
------
output the number of pairs of indices (i,j) such that
i<j and Ai is similar to Aj in a single line

Sample Input                      Sample Output
------------                      -------------
8                                 6
1 3 5 7 8 2 5 7



"""
count=0
map1=[]
for i in range(0,N):
    for j in range(0,N):
        if((A[i]==A[j]+1) or (A[j]==A[i]+1)):
                count+=1
                map1.append((i,j))
        for k in range(0,N):
            if((((A[i]==A[j]+1) or (A[j]==A[i]+1)) and ((A[k]==A[j]+1) or (A[j]==A[k]+1))))  :
                count+=1
                map1.append((i,k))
            if((((A[i]==A[j]+1) or (A[j]==A[i]+1)) and ((A[j]==A[k]+1) or (A[k]==A[j]+1)))):
                count+=1
                #map1.append((i,k))
            if((((A[i]==A[j]+1) or (A[j]==A[i]+1)) and ((A[k]==A[i]+1) or (A[i]==A[k]+1)))):
                count+=1
                map1.append((j,k))
list1 = set(map(lambda x: tuple(sorted(x)),map1))
list2=[]
for x,y in list1:
    if abs(x-y)>0:
        list2.append((x,y))
return len(list2)

N = input()
A = map(int, raw_input().split())
out_ = SimilarElementsPairs(A,N)
print(out)_