# to print anything
print('Hellow ayush')
#to print multiple line
print("""name : Ayush age:20 loves:S.j""")
#to assignment a value to a variable
a=10
print(a)
#to take input from the user
name= input('enter name:')
print('hellow', name)
#to sum and usska datatypes and usska conversion | in 'b' 1.1(float) is converted into integer jo ki h '1'
a=10
integer_number=2
float_number=1.1
b=int(float_number)
sum = a + integer_number + float_number + int(float_number)
print("sum ayega :", sum)
#sum(+) operator
a= 10
b= a+ 5
sum = a+b
print('sum ayega:', sum)
#diff(-) operator
a=2.4
b=int(a)
diff= a-b
print('difference ayega', diff)
#multiplication(*) operator
a=6.7
b=float(a)
product=a*b
print("product ayega:" , product)
#division(/) operator eg- 6.7/6.7
div=a/b
print('division ayega:', div)
#quostient(//) operator same example jo ki uper h
questient=a//b
print('questient ayega:',questient)
#remainder(%) operator same example jo ki uper h
remainder=a%b
print("remainder ayega", remainder)
#raise to power (**) operator
a=2
b=3
cube= a**b
print('2 ka cube ayega:',cube)
#Multipilcation se ek string ko repeat v kar sake h
a= "FAHHHH!!!"
b= a*3
print(b)
#Assignment operator (+=,-=,*=,/=,//=,**=)
x=10
x+=2 #x=x+2
print(x)
y=2
y-=1 #y=y-1
print(y)
z=2
z*=2 #z=2*2
print(z)
m=10
m/=2 #m/2
print(m)
n=11
n//=2 #questient
print(n)
k=5
k%=2 #remainder
print(k)
#comparision operator (<,>,==,<=,>=)
a,b,c=1,5,2
print(a<c)
print(b==a)
print(c<a)
print(a<=c)
print(b>=a)
#Logical operator (and, or, not(!=))
print(a==c and b>=c)
print(b<=c or a<b)
print(a!=8) #a is not equal to 8 is true
print(not(a!=8))  #true ka not karenge toh false ayega
#if operators

a=10 #ex-1
if a>1:
  print('a one se bara h')
else :
  print("pagal h kya")


a=5 #ex-2
if a<1:
  print("a bara h 1 se")
else :
  print("pagal h kya chota kayse hoga?")


num= int(input("enter a no:")) #ex-3
if num>0 :
  print(num,"is positive")
else :
  print(num,"is negative")

#elif (if...else) operators
num = float(input("enter a no:"))
if num>0 :
  print(num,"is positive")
elif num==0:
  print("no is zero")
elif num==1:
  print("no is one") #multiple statement desakete h
else:
  print(num,"is negative")

#PROJECT 1= SIMPLE CALCULATOR
print("btao kya calculate karna h?")
operator= input("koi 1 choose karo +,-,/,*:" )
n1=float(input("1st no daalo :"))

n2=float(input("2nd no daalo :"))
if operator== '+':
    print(n1,'+',n2,"=",n1+n2)
    print("sum ayega :",n1+n2)
elif operator == '-':
    print(n1,'-',n2,"=",n1-n2)
    print("difference ayega :",n1-n2)
elif operator =='*':
    print(n1,'*',n2,"=",n1*n2)
    print(" product ayega :",n1*n2)
elif operator=='/':
    print(n1,'/',n2,"=",n1/n2)
    print("division hoga :",n1/n2)
else :
    print("unnhi 4 operator me se ek chunna tha BEWAKOOF!!" )
#While loop
a=2
i=0
while i<=a : #condition jab tak true h
  print('ayush')
  i=i+1 #i=0,1,2,3 pe print hoga
#while else loop
a=3
n=2
i=0
while i<=a:
    print("AYUSH")
    i=i+1
else :   #while loop hone k baad chalega
    print("SIN")
#For loop...(Sum of n natural numbers)
list_1 = [ 'A' ,'B' ,'C']
range_1 = range(1,11) #1 se 10 tak
for item in list_1 :
    print(item)
for i in range_1 :
    print(i)
#to find sum of n natural no.
    numbers = range(1,101) #1 to 100 tak
    sum = 0
for item in numbers:
  sum=sum+item #(sum=0+1=1,sum=1+2=3....)

print('Sum=',sum)

#for loop and else loop (ERROR H SYAD)

number= range(1, 10) #1 se 9 tak
add = 0           #initial sum zero h
for item in number:
    add=add+item
    print('SUM :',add)

else :
  print('yhi answer h')

#creating a table
n=12
no = range(1, 11)
for i in no :
  print(n,'x',i ,'=',n*i)

#Break and continue python
number= [1,73,83,-28,9,-98]

for val in number : #ex-1
  if val < 0 : #value -ve hote hi loop close ho gya
    break
  print(val)

number =[22222,73,-28,-23,18]
for val in number: #ex-2
  if val< 0 : #-ve no exclude ho gya
    continue 
  print(val)
