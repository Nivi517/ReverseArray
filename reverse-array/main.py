def reverse(l):
    s=[]
    for i in l:
        s.append(i)
    list2=[]
    for i in range(0,len(s)):
        temp=s.pop()
        list2.append(temp)
    return list2
n=int(input())
list1=list()
while(n):
  l=int(input())
  list1.append(l)
  n-=1
print(list1)
print(*reverse(list1),sep=',')
    
