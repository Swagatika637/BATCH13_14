# for i in range(20):
#     print(range(20))


# li = [20,70,54,89,45,]
# for i in li:
#    print(i)

# for i in li:
#    i+=5
#    print(i)


# #wap and print the even number taken from the enduser?
# a = int(input(""))
# for i in range(a):
#  if i%2==0:
#     print(i)

# #wap and print the odd number taken from enduser?
# b = int(input(""))
# for i in range(b):
#    if i%2!=0:
#       print(i)


#wap to put odd and even numbers in different list?
# list = [20,30,10,45,78,64,12]

# even_li=[]
# odd_li=[]
# for i in list:
#     if i%2==0:
#         even_li.append(i)
#     else:
#         odd_li.append(i)
# print(even_li)
# print(odd_li)


#print 10 numbers
# for i in range(10):

#     print(i)
 

#print a pattern in for loop/

num = int(input('enter your number:-'))
# for i in range(num):
#     print('*'*(i+1))

# for i in range(5):
#     print('*')


for i in range(2,num+1,2):
    if i%2==0:
        print('*'*i)

