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
