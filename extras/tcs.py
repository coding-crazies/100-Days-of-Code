# def calculate(ip):
#     no = []
#     no.append(int(ip))

#     for i in range(len(ip)):
#         no.append(int(ip[i]))
#     for i in range(len(ip)-1):
#         s = ip[i]+ip[i+1]
#         if int(s) not in no:
#             no.append(int(s))
#     sum = 0
#     for i in range(len(no)):
#         sum += no[i]

#     return sum


# ip = input()
# print(calculate(ip))

a=input()
b=a.split()
sum=int(a)
for i in b[0]:
    sum=sum+int(i[0])
if(len(b[0])>2):
    for j in range(len(b[0])-1):
        z=int(b[0][int(j)])
        y=int(b[0][int(j+1)])
        w=str(z)+str(y)
        sum=sum+(int(w))
print(sum)