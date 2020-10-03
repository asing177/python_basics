# Input : X = [[1, 7, 3],
#             [3, 5, 6],
#             [6, 8, 9]]
#        Y = [[1, 1, 1, 2],
#            [6, 7, 3, 0],
#            [4, 5, 9, 1]]
#
# Output : [55, 65, 49, 5]
#          [57, 68, 72, 12]
#          [90, 107, 111, 21]

A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

def matmul(A,B,result):
    for i in range(len(A)):

        # iterating by coloum by B
        for j in range(len(B[0])):

            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


print(matmul(A,B,result))

