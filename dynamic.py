########################################
#########01背包####################

# weight物品的重量，n物品个数， w:背包可承载的重量
def f(weight, n, w):
    states = [[0 for i in range(w+1)]for i in range(n)]
    states[0][0] = True
    if weight[0] <= w:
        states[0][weight[0]] = True
    for i in range(1, n):
        for j in range(w+1):
            if states[i-1][j]:
                states[i][j] = states[i-1][j]
        for j in range(w+1-weight[i]):
            if states[i-1][j]:
                states[i][j+weight[i]] = True
    for i in range(w, -1, -1):
        if states[n-1][i]:
            return i
    return 0

def f1(weight, n, w):
    states = [0 for i in range(w+1)]
    states[0] = True
    if weight[0] <= w:
        states[weight[0]] = True
    for i in range(1, n):
        for j in range(0, w+1-weight[i]):
            if states[j]: states[j+weight[i]] = True

    for i in range(w, -1, -1):
        if states[i]:
            return i
    return 0
print(f1([2, 2, 4, 6, 3], 5, 9))



def yanghuiTriangle(matrix):
    state = [[0 for i in range(len(matrix[len(matrix)-1]))] for i in range(len(matrix)) ]
    state[0][0] = matrix[0][0]
    for i in range(1, len(matrix)):
        for j in range(len(matrix[i])):
            if j == 0:
                state[i][j] = state[i-1][j] + matrix[i][j]
            elif j == len(matrix[i])-1:
                state[i][j] = state[i-1][j-1] + matrix[i][j]
            else:
                top1 = state[i-1][j]
                top2 = state[i-1][j-1]
                state[i][j] = min(top1, top2) + matrix[i][j]
    minDis = state[len(matrix)-1][0]
    for i in range(len(matrix[len(matrix)-1])):
        if state[len(matrix)-1][i] < minDis:
            minDis = state[len(matrix)-1][i]
    return minDis
matrix = [[5],[7, 8], [2, 3, 4], [4, 9, 6, 1], [2, 7, 9, 4, 5]]
print(yanghuiTriangle(matrix))


def rectangle(matrix):
    states = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
    states[0][0] = matrix[0][0]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0:
                states[i][j] = states[i][j-1] + matrix[i][j]
            elif j == 0:
                states[i][j] = states[i-1][j] + matrix[i][j]
            else:
                states[i][j] = min(states[i-1][j], states[i][j-1]) + matrix[i][j]
    return states

matrix = [
    [1, 3, 5, 9],
    [2, 1, 3, 4],
    [5, 2, 6, 7],
    [6, 8, 4, 3]
]
print(rectangle(matrix))

len = int(input())

for i in range(len):
    nums = list(map(int, input().split()))
    print(sum(nums))