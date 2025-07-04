'''write a code to check the given number is even or odd using in-direct recursive method with boolean output
input:5
output:FALSE'''
def evn(n):#n=5
    if n==0:
        return True
    return odd(n-1)#odd(4)
def odd(n):
    if n==0:
        return False
    return evn(n-1)
num=int(input("Enter a number:"))#if n=5
print(num,"is even?",evn(num))#num=5