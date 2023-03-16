# 生成空幻方的函数
def cre_empty_matrix(n):
    """生成空幻方"""
    mat = [[] for num in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            mat[i].append(0)
    return mat


# 构造奇数阶幻方的函数
def odd_matrix(n):
    """写奇数阶幻方"""
    # 创建空幻方
    matrix = cre_empty_matrix(n)
    # 进行坐标构建并找到“1”的位置
    sn = n ** 2
    xp = (n + 1) / 2
    xpos = int(xp - 1)
    ypos = 0
    matrix[ypos][xpos] = 1
    # 构造幻方
    for k in range(2, sn + 1):
        # 确定下一个坐标的位置
        if xpos == n - 1:
            nextx = 0
        else:
            nextx = xpos + 1
        if ypos == 0:
            nexty = n - 1
        else:
            nexty = ypos - 1
        if matrix[nexty][nextx] != 0:
            nexty = ypos + 1
            nextx = xpos
        # 转移坐标并进行赋值
        xpos = nextx
        ypos = nexty
        matrix[ypos][xpos] = k

    return matrix


# 构造4K阶幻方
def double_even_matrix(n):
    """构造4K阶幻方"""
    # 构造一个按序排列的n阶幻方
    m = int(n / 2)
    matrix = [[] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            t = n * i + j + 1
            matrix[i].append(t)

    # 进行转换
    for i in range(0, m):
        if i % 2 == 0:
            j = 0
        else:
            j = 1
        while j < m:
            t = matrix[i][j]
            matrix[i][j] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = t
            t = matrix[i][n - j - 1]
            matrix[i][n - j - 1] = matrix[n - i - 1][j]
            matrix[n - i - 1][j] = t
            j = j + 2

    return matrix


# 按排列顺序构造等差的奇数阶幻方
def cre_spec_matrix(n, num):
    """按排列顺序构造等差的奇数阶幻方。"""
    mat = odd_matrix(n)
    addition = num * (n**2)
    for t in range(0, n):
        for s in range(0, n):
            mat[t][s] = mat[t][s] + addition
    return mat


# 构造4k+2阶幻方
def single_even_matrix(n):
    """构造4K+2阶幻方"""
    # 构造一个空的n/2阶幻方
    m = int(n / 2)
    matrixA = cre_spec_matrix(m, 0)
    matrixB = cre_spec_matrix(m, 2)
    matrixC = cre_spec_matrix(m, 3)
    matrixD = cre_spec_matrix(m, 1)

    # 寻找需要对换的数并对换
    k = int((n - 2) / 4)
    # 对换AC矩阵的上下角
    for il in range(0, k):
        for jl in range(0, k):
            # 对换左侧上区
            trans = matrixA[il][jl]
            matrixA[il][jl] = matrixC[il][jl]
            matrixC[il][jl] = trans
            # 对换左侧下区
            trans = matrixA[m - 1 - il][jl]
            matrixA[m - 1 - il][jl] = matrixC[m - 1 - il][jl]
            matrixC[m - 1 - il][jl] = trans
    # 对换AC矩阵的中部
    for ilm in range(k, 2 * k):
        trans = matrixA[k][ilm]
        matrixA[k][ilm] = matrixC[k][ilm]
        matrixC[k][ilm] = trans
    # 对换BD矩阵
    if n != 6:
        for ir in range(0, m):
            for jr in range(2, k + 1):
                trans = matrixB[ir][jr]
                matrixB[ir][jr] = matrixD[ir][jr]
                matrixD[ir][jr] = trans

    # 组合幻方
    matrix = cre_empty_matrix(n)
    for i in range(0, m):
        for j in range(0, m):
            matrix[i][j] = matrixA[i][j]
            matrix[i][j + m] = matrixB[i][j]
            matrix[i + m][j] = matrixC[i][j]
            matrix[i + m][j + m] = matrixD[i][j]

    return matrix
