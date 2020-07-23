import numpy as np

#A = np.array([[1, 2, 3], [3, 4, 5]])
#print(A)

# for x in A:
#   #print(x)

# a = np.arange(4).reshape(2,2)
# #print(a)
#
# with np.nditer(a, op_flags=['readwrite']) as it:
#     for x in it:
#         x[...] = 2 * x
#
# a[0,0]=5
#
# for  i in (0,1):
#  print(a[i])
#  print(i)

#print(a[1][1])

#print(a)


# rows = 6
# for num in range(rows):
#     for i in range(num):
#         print(num,i)  # print number
#     # line after each row to display pattern correctly
#     print(" ")

A = [[1, 4],
    [-5, 8]]

for i in range(2):
    for j in range(2):
        #print(A[0][0])
        print(A[i][j], end=" ")
        # if A[i][j]>A[i][j+1]:
        #     print("Moving Right and suck")
        # elif A[i][j]>A[i+1][j]:
        #     print("Moving Down and suck")


        #print()