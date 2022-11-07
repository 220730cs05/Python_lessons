import random
n = 100
numbers = list(range(1,n+1))
x = numbers.pop(random.randint(1,n+1))
print(x)
# find x

#      1st way
# for i in range(1,n+1):
#     if i not in numbers:
#         print(i)
#         break


#      2nd way
total = n * (n+1) // 2
print(total - sum(numbers))