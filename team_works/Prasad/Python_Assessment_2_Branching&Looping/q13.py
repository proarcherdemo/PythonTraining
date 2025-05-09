# #q13
# for i in range(1,6):
#     for x in range(0,i):
#         print(i,end=" ")
#     print()
#
# #q14
# for i in range(1,6):
#     for x in range(1,i+1):
#         print(x,end=" ")
#     print()

#q15
# y=1
# for i in range(6,1,-1):
#     for x in range(1,i):
#         print(y,end=" ")
#     y+= 1
#     print()

# z=5
# for i in range(5,0,-1):
#     for x in range(1,i+1):
#         print(z,end=" ")
#     print()

# for i in range(6,1,-1):
#     for x in range(0,i):
#         print(x,end=" ")
#     print()

# for i in range(1,10,2):
#     for x in range(1,i+1,2):
#         print(i,end=" ")
#     print()

# for i in range(5,0,-1):
#     for x in range(i,0,-1):
#         print(i,end=" ")
#     print()

# for i in range(1,6):
#     for x in range(i,0,-1):
#         print(x,end=" ")
#     print()

# for i in range(1,6):
#     for x in range(i,0):
#         print(x,end=" ")
#     print()

for i in range(5,0,-1):
    for x in range(1,i+1):
        if(x==i):
            print(x,end=" ")
        else:
            print(" ",end=" ")
    print()
