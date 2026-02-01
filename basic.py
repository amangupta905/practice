# palindrome

x="121"

y=""

for i in range(len(x)):
    y+=x[i]

if(x==y):
    print("its palindrome")
else:
    print("not palindrome")

#sorting
# x=[1,2,3,2,3,4,5,6]

# for i in range(len(x)-1):
#     if(x[i]>x[i+1]):
#         x[i],x[i+1]=x[i+1],x[i]

# print(x)

def fect(num):
    if num==0 or num==1:
       return 1
    else:
        return num*fect(num-1)

print(fect(5))