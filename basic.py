# palindrome

# x="121"

# y=""

# for i in range(len(x)):
#     y+=x[i]

# if(x==y):
#     print("its palindrome")
# else:
#     print("not palindrome")

#sorting
# x=[1,2,3,2,3,4,5,6]

# for i in range(len(x)-1):
#     if(x[i]>x[i+1]):
#         x[i],x[i+1]=x[i+1],x[i]

# print(x)

# def fect(num):
#     if num==0 or num==1:
#        return 1
#     else:
#         return num*fect(num-1)

# print(fect(5))

# frequency

# x=[1,2,3,1,2,3,4,5,4,5,6,6,7,77,6,4,3]
x="helloworldpythonok"

y={}

for i in x:
    if i in y:
        y[i]+=1
    else:
        y[i]=1
print(y)


        




