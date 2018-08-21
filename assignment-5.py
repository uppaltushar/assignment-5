#1
year=int(input("enter the year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(' leap year')
        else:
            print('not a leap year')
    else:
        print('leap year')
else:
    print('not a leap year')

#2
length=int(input("enter the length :"))
breadth=int(input("enter the breadth :"))
if(length==breadth):
    print('it is a square')
else:
    print('it is a rectangle')

#3
n=int(input("enter the number of people"))
a=[]
for i in range (n):
    a.append(input('enter the age'))
    
o=max(a)
y=min(a)
print('the oldest is {} and youngest is{}'.format(o,y))

#4
age=int(input('enter age :'))
sex=input('enter sex m or f :')
martial=input('enter martial y or n :')
if(age<20 or age>60):
    print('ERROR')
else:
    if(sex=='f' or sex=='F'):
        print('work only in urban area')
    if(sex=='m' or sex=='M' and age>20 and age<40):
        print('work anywhere')
    elif(sex=='m' and age>40 and age<60):
        print('work urban areas')

  
#5
unit=int(input("enter unit that are purchased by user :"))
total=unit*100
if (total>1000):
    discount=(total*10)//100
    final=total-discount
    print('the total cost is',final)
else:
    print('the total cost is ',total)

#loops
#1
b=[]
for i in range (1,10):
    a=int(input("enter"))
    b.append(a)
for i in b:
    print(i)

#2
while True:
    print('python')

#3
n=int(input("enter"))
a=[]
c=[]
for i in range(1,n+1):
    b=int(input("enter"))
    a.append(b)
for i in a:
    d=i**2
    c.append(d)
print(c)
#4
li1=[]
li2=[]
li3=[]
li4=[]
a=int(input("Enter total number of inputs"))
for i in range(a):
    b=input("Enter elements of list")
    li1.append(b)
for i in li1:
    if(i.isdigit()):
        li2.append(i)
    elif(i.isalpha()):
        li3.append(i)
    else:
        li4.append(i)
print(li2)
print(li3)
print(li4)

#5

p=[]
for i in range(1,101):
    if(i>1):
        flag=False
        for j in range(2,i):
            if(i%j==0):
                flag=True
        if not flag:
            p.append(i)
print(p)

#6

for i in range(5):
    for j in range(i):
        print("*",end='')
    print()


#7


li8=[]
n=int(input("Enter number of elements of list"))
for i in range(n):
    a=int(input("Enter element"))
    li8.append(a)
num=int(input("Enter the number you want to delete from list"))
x=li8.count(num)
for i in range(x):
    y=li8.index(num)
    del(li8[y])
print(li8)








