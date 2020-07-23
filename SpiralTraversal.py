
R = 2
C = 2

DirtCollected=[];
print(DirtCollected)


# Function to print
# the required traversal
def counterClockspiralPrint(m, n, arr):
    k = 0;
    l = 0

    # k - starting row index
    # m - ending row index
    # l - starting column index
    # n - ending column index
    # i - iterator

    cnt = 0


    total = m * n

    for p in range(1,4):


     while (k < m and l < n):
        if (cnt == total):
            break

        # Print the first column
        # from the remaining columns
        for i in range(k, m):
            print(arr[i][l], end=" \n")
           # print('Position1')

            print(i,l)
            if arr[i][l]>0:
                arr[i][l] == 0
                print('Suck')
            else:
                print("Move Ahead")

            DirtCollected.insert(p,arr[i][l])
            cnt += 1



        l += 1

        if (cnt == total):
            break

        # Print the last row from
        # the remaining rows
        for i in range(l, n):
            print(arr[m - 1][i], end=" \n")
          #  print('Position2')
            print(m-1, i)
            print(i, l)
            if arr[m - 1][i] > 0:
                arr[m - 1][i]=0
                print('Suck')
            else:
                print("Move Ahead")
            DirtCollected.insert(p, arr[m - 1][i])
            cnt += 1

        m -= 1

        if (cnt == total):
            break

        # Print the last column
        # from the remaining columns
        if (k < m):
            for i in range(m - 1, k - 1, -1):
                print(arr[i][n - 1], end="\n ")
               # print('Position3')
                print(i,n-1)
                print(i, l)
                if arr[i][n - 1] > 0:
                    arr[m - 1][i]=0
                    print('Suck')
                else:
                    print("Move Ahead")
                DirtCollected.insert(p,arr[i][n - 1])
                cnt += 1
            n -= 1

        if (cnt == total):
            break
        if (l < n):
            for i in range(n - 1, l - 1, -1):
                print(arr[k][i], end=" \n")
                ##print('Position4')
                print(k, i)
                print(i, l)
                if arr[k][i] > 0:
                    arr[m - 1][i]=0
                    print('Suck')
                else:
                    print("Move Ahead")
                DirtCollected.insert(p,arr[k][i])
                cnt += 1




            k += 1




# Driver Code
arr = [[1, 2],
       [0, 6]]


counterClockspiralPrint(R, C, arr)