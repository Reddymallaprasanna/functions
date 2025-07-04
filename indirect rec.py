#indirect recursuion
def one(n):
    if n>0:
        print("One:",n)
        two(n-1)
def two(n):
    if n>0:
        print("Two:",n)
        one(n//2)
num=int(input("Enter a value:"))
one(num)