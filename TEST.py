# a = '123'
# print(set(a))

# n=int(input())
# if n%4==0:
#     a = n // 2
#     b = n % 2
#     print(a + 1)
# elif n>3:
#     a=n//2
#     b=n%2
#     print(a+2+b)
# else:
#     match n:
#         case 1:
#             print(1)
#         case 2:
#             print(2)
#         case 3:
#             print(3)



# x1,v1,x2,v2 = map(int,input().split())
# t = abs(x1-x2)*(v1-v2)
# if (t*v1+x1) == (t*v2+x2):
#   print('YES')
# else:
#   print('NO')
# print(abs(5-6))


# print()


# a=1e9-1#int(input())
# q=1
# m=0
# qadam = (m+1)+(a-1)*3
# result = int(((1+qadam)*a)/2)
# print(result)



# for i in range(1,2):
#     for j in range(1,10):
#         karra = f"{i} x {j} = {i*j} \t|\t"
#         karra += f"{i+1} x {j} = {(i+1)*j} \t|\t"
#         karra += f"{i+2} x {j} = {(i+2)*j} \t|\t"
#         karra += f"{i+3} x {j} = {(i+3)*j} \t|\t"
#         karra += f"{i+4} x {j} = {(i+4)*j} \t|\t"
#         karra += f"{i+5} x {j} = {(i+5)*j} \t|\t"
#         karra += f"{i+6} x {j} = {(i+6)*j} \t|\t"
#         karra += f"{i+7} x {j} = {(i+7)*j} \t|\t"
#         karra += f"{i+8} x {j} = {(i+8)*j} \t|\t"
#         print(karra)

# n = int(input('N: '))
# for son in range(1,n):
#     if son % 15 == 0:
#         print(son, 'FIZBUZ')
#     elif son % 5 == 0:
#         print(son, 'BUZ')
#     elif son % 3 == 0:
#         print(son, 'FIZ')
#     else:
#         print(son)


name = input('name: ')
print('Yes') if name == name[::-1] else print('No')


