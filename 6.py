def T(n):
    if n==1 or n==2:
        return n
    else:
        return T(n-1)+T(n-2)
n=int(input(台阶数：))
if n>=0:
    print(T(n))
elif n<0:
    print("error(n<0)")
else:
    pass

