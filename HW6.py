# list=[]
# listch=[]
# listn=[]
# N=int(input())
# for i in range (1, N+1):
#     a=int(input())
#     list.append(a)
#     if a%2==0:
#         listch.append(a)
#     else:
#         listn.append(a)
# print(listch)
# print(listn)
# if len(listch)>len(listn):
#     print('yes')
# else:
#     print('no')

# def add(n):
#     s=0
#     for i in range(n):
#         l = input()
#         a = list(l)
#         a1 = int(a[i])
#         s=s+a1
#     return s
# print(add(3))

# def cv(fn0, sn0, adr0, em0, ph0, edu0, exp0):
#     resume={'first name':fn0, 'surname':sn0, 'adress':adr0, 'email':em0, 'phone':ph0,'education':edu0,'experiens':exp0}
#     type = input('Choose the type of information:')
#     return resume.get(type)
# fn=input()
# sn=input()
# adr=input()
# em=input()
# ph=input()
# edu=input()
# exp=input()
# cv1 = cv(fn,sn,adr,em,ph,edu,exp)
# print(cv1)

# def fib(n):
#     if n==1 or n==2:
#         return 1
#     return fib(n-1)+fib(n-2)
# a=int(input())
# ch=fib(a)
# print(ch)

def st(n):
    while True:
        a=n/2
        if a==2:
            return True
            break
        elif a < 2:
            return False
            break
n1=int(input())
b=st(n1)
print(b)