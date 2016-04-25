n, k = input().split()
n=int(n)
k=int(k)
def silnia(a):
    if a>1:
        return a*silnia(a-1)
    elif a in (0,1):
        return 1
x=silnia(n)
y=silnia(k)
z=silnia((n-k))
newton=int(x/(y*z))
print("wynik to:")
print(newton)