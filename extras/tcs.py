def check(n):
    if n<=0:
        print("Wrong Input")
        return 
    re=pow(n,4)
    res=re%10
    if res== n:
        print('True')
    else:
        print('False')
        
n=int(input())      
check(n)