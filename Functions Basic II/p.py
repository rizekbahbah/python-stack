def countdown(x):
    for i in range(x, -1, -1):
        print(i)
countdown(20)

def printReturn(x):
    print(x[0])
    return x[1]

numbers= [1,2]
printReturn(numbers)

def firstlength(x):
    return (x[0]+len(x))
nums=[1,2,3,4,5]
print(firstlength(nums))

def greater(t):
    h=t[1]
    for i in range(len(t)-1,-1,-1):
        if (t[i] <= h) :
            t.pop(i)
    return t
c=[5,4,3,2,1,4]
print(greater(c))
print(len(c))
print(c)


def length_and_value(a):
    b=[]
    for i in range(0,a[0],1):
        b.append(a[1])
    return b

l=[4,7]
print(length_and_value([4,7]))




