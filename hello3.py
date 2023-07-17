
"""
#store
def thing():
    print('HELLO PEACE!')
    print('hello joy')
#reuse
thing()
"""
"""
def param1(p1):
    if p1 =='en':
        return 'hola'
    elif p1=='benny':
        return'aloha'
    else:
        return 'luolua'
print('hello',param1('benny'))
"""

"""
def greet():
    return 'Hello there' 
greet()
"""
#prompt entry in the function, add and return sum?
#function to amke use of values input by user?
"""
x=input('enter first number:')
try:
        b=int(x)
except:
        print('please key in a digit!')
#insert loop to ensure if try fails the first number prompt repeats        
y=input('enter second number:')
z=input('enter third number:')
def addnum(x,y,z):
    a=x+y+z
    return a
print(addnum(10,10,10))
"""
"""
n=1
while n>0:
    print(n)
    break
    #n=n-1
print('no longer greater than zero')
print(n)
"""
"""
while True:
    line=input('> ')
    if line[0]=='#':
        continue
    if line=='done':
        break
    print(line)
print('we are done with this')
"""
"""
for i in [5,4,3,2,1]:
    print(i)
print('not in our menu')
"""
"""
#0 is a flag value
largest=0
#None is a flag value
smallest=None
count=0
total=0
found=False
print(largest)
print('Initial total is:', total)
for num in [5,10,15,20,2,3,1]: 
    count=count+1
    total=total+num
    average=total/count
    rem=total%count
    if num==5:
        found=True
        print('number being sought after in the list exists:', num)
        print(found, num)
    if num>largest:
        largest=num
    print(count,largest, num)
    if smallest is None:
        smallest=num
    elif num<smallest:
        smallest=num
    print('smallest number is', smallest) 
print('our largest number is:', largest)
print('final total is:', total)
print('average value is:',average)
print('remainder is:', rem)
"""
"""
n=0
friends=['ali','mohamed','fredy']
for friend in friends:
    n=n+1
    print(n,'happy eid ul adha:',friend)
print('Have a good one!')
"""
total=0
count=0
largest=None
smallest=None
while True:
    a=input('enter a number:')
    #if a=='DONE':
        #break
    try:
        b=float(a)
        #print(b)
    except:
        print('Error, enter numbers!')
        continue
    if largest is None:
        largest=b
    elif b>largest:
        largest=b
        print('largest number so far is:', largest)
    if smallest is None:
        smallest=b
    elif b<smallest:
        smallest=b
        print('smallest number so far is:', smallest)
    count=count+1
    total=total+b
    average=total/count
    rem=total%count
#print(total,count,average,rem)
#print(largest)


print('hello')
print('wooo')
print('.')


