#code starts here
x = input()
y = x.split(' ')
num = []
oper = []
for i in range(len(y)):
    if i % 2 == 0:
        num.append(float(y[i]))
    else:
        oper.append(y[i])
print (oper[0])
for j in range(len(oper)):
    if (oper[j]=='+'):
        num[0] = num[0] + num[1]
        del(num[1])
    if (oper[j]=='-'):
        num[0] = num[0] - num[1]
        del(num[1])
    if (oper[j]=='*'):
        num[0] = num[0] * num[1]
        del(num[1])
    if (oper[j]=='/'):
        num[0] = num[0] / num[1]
        del(num[1])


if num[0] % 1 == 0:
    num[0] = int(num[0])
    
print ("Result: ", num[0])
