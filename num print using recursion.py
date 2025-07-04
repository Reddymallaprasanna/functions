'''recursions are of 
head

indirect
nested
'''
#linear/head
def hrec(n):
    if n==0:
        return
    hrec(n-1)
    print(n)
num=int(input("enter the value:"))
hrec(num)
