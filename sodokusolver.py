import math
import random
import copy
import time
import numpy as np
# isValid(puzzle matrix m; aTry form of x, y, value)
# matrix in square where (x to the right, y down direction of vector)
# assume 0 based counting for matrix
def isValid(m, aTry):
    # assert that p is square matrix and y is 3-tuple with value between 0 and 9 inclusive
    # print ("matrix m = ", m, "aTry = ", aTry)
    # search row for duplicate and return 0
    xTry = aTry[0]
    yTry = aTry[1]
    val = aTry[2]
    if val < 1 or val > 9 :
        return -1 # assert attempts have valid range from 0 through 9
    s = len(m[0]) # len returns dimension with 1 based counting
    for i in range(s):
        #print("interation =", i, "col =", xTry, "row =", yTry, "val =", val)
        if val == m[xTry][i]: # search along y axis of matrix for column specified by aTry[0]
            return -2, "duplicate", aTry, i
        if val == m[i][yTry]: # search along x axis of matrix for row specified by aTry[1]
            return -3, "duplicate", aTry, i
    # check entry is not duplicated within the 9 cell square
    xcell = (xTry / 3) * 3
    ycell = (yTry / 3) * 3
    for ii in range(0, 3):
        for jj in range(0, 3):
            #print "debug", xcell+ii, ycell+jj, xTry, ii, yTry, jj
            #print (xcell, ycell, ii, jj, val)
            if val == m[xcell+ii][ycell+jj] :
                return -4, "duplicate in cell", aTry, ii, jj

    return 1 # must be valid

# feeble attempt 1
# given matrix m, pick non-zero entry; return 0,0,0 if no more non-zero entries available
def getNext(m) :
    l = len(m[0])
    for i in range (l) :
        for j in range (l) :
            if 0 == m[i][j] :
                return 1,i,j
    return 0,0,0
#print(getNext(p))

#feeble attempt 2
def getNextRandom(m) :
    l = len(m[0])
    for z in range(200) :
        i = random.randint(0,l-1)
        j = random.randint(0,l-1)

        if 0 == m[i][j] :
            #print (i, j)
            return 1,i,j
    return 0,0,0

def countzeros(x,y,m):
    l = len(m[0])
    accum = 0
    for i in range (l):
        if 0 == m[x][i] :
            accum = accum + 1
        if 0 == m[i][y]:
            accum = accum + 1
    return accum


# for each non-zero entry, calculate the which cell is the most constrained by non-zero row and column entries
# the least number of zero contraints will the the next time returned
# if no zero entries can be found 0,0,0 is returned
# select cells random proportional to how contrained a cell is
def getNextConstrained(m):
    l = len(m[0])
    minzeros = 99
    for i in range (l) :
        for j in range (l) :
            if 0 == m[i][j] :
                if random.randint(1,10) < 4 : # don't always pick the cell to work on to add randomness to the cell selection
                    zeros = countzeros(i,j,m)
                    if zeros < minzeros :
                        xmin = i
                        ymin = j
                        minzeros = zeros

    if 99 == minzeros:
        return 0,0,0 # no zeros found
    #print ("minzeros, x, y", minzeros, xmin,ymin )
    return 1, xmin, ymin




# while getNext is sucessful,
#   for each number from 1 through 9; check if valid
#       if valid then recursively call function again on new matrix
#   if all entries in matrix have been filled we must have found a solution; print solution
def solve(m, depth) :
    r,x,y = getNextConstrained(m)
    #print "solve function called", r, x, y
    if 0 == r :
        return "solved!", m

    for i in range(40): # warning,
        rv = random.randint(1,9)
        o1 = isValid(m, [x, y, rv])
        if 1 == o1 :
            m[x][y] = rv
            #print "new sodoku entry", x, y, rv, mtmp
            solve(m, depth+1)
    return m

# calculate the number of zeros in the matrix (lower the better; 0 means puzzle solved
def grade(m):
    l = len(m[0])
    count = 0
    for i in range (l) :
        for j in range (0,l) :
            if 0 == m[i][j] :
                count = count + 1


    return count

# sample sodoku puzzles
p1 = [1,2,5,0,0,0,0,0,0]
p2 = [4,3,6,0,0,0,0,0,0]
p3 = [0,0,0,0,0,0,0,0,0]
p4 = [0,0,0,0,0,0,0,0,0]
p5 = [0,0,0,0,0,0,0,0,0]
p6 = [0,0,0,0,0,0,0,0,0]
p7 = [0,0,0,0,0,0,0,0,0]
p8 = [0,0,0,0,0,0,0,0,0]
p9 = [0,0,0,0,0,0,0,0,0]

pa = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

p1 = [2,1,0,0,0,8,3,0,0]
p2 = [0,5,0,7,0,0,0,0,0]
p3 = [6,8,7,0,0,2,0,9,0]
p4 = [4,0,0,9,0,0,6,0,0]
p5 = [9,6,5,0,0,0,7,4,2]
p6 = [0,0,8,0,0,6,0,0,5]
p7 = [0,7,0,8,0,0,5,3,9]
p8 = [0,0,0,0,0,1,0,7,0]
p9 = [0,0,6,5,0,0,0,2,4]
pb = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

p1 = [0,0,0,0,0,0,0,0,0]
p2 = [0,0,0,0,0,0,0,0,0]
p3 = [0,0,0,0,0,0,0,0,0]
p4 = [0,0,0,0,0,0,0,0,0]
p5 = [0,0,0,0,0,0,0,0,0]
p6 = [0,0,0,0,0,0,0,0,0]
p7 = [0,0,0,0,0,0,0,0,0]
p8 = [0,0,0,0,0,0,0,0,0]
p9 = [0,0,0,0,0,0,0,0,0]
pc = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

p1 = [0,0,1,8,3,0,0,0,0]
p2 = [9,6,5,0,0,0,0,0,0]
p3 = [0,0,0,0,1,0,9,0,0]
p4 = [4,0,0,0,0,0,0,1,0]
p5 = [0,0,9,6,0,4,3,0,0]
p6 = [0,8,0,0,0,0,0,0,2]
p7 = [0,0,7,0,9,0,0,0,0]
p8 = [0,0,0,0,0,0,5,4,8]
p9 = [0,0,0,0,2,5,1,0,0]
pd = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

p1 = [1,0,0,0,0,7,0,9,0]
p2 = [0,3,0,0,2,0,0,0,8]
p3 = [0,0,9,6,0,0,5,0,0]
p4 = [0,0,5,3,0,0,9,0,0]
p5 = [0,1,0,0,8,0,0,0,2]
p6 = [6,0,0,0,0,4,0,0,0]
p7 = [3,0,0,0,0,0,0,1,0]
p8 = [0,4,0,0,0,0,0,0,7]
p9 = [0,0,7,0,0,0,3,0,0]
pe = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

# 2012 finnish mathematician Arto Inkala claimed worlds hardest sodoku puzzle
p1 = [8,0,0,0,0,0,0,0,0]
p2 = [0,0,7,5,0,0,0,0,9]
p3 = [0,3,0,0,0,0,1,8,0]
p4 = [0,6,0,0,0,1,0,5,0]
p5 = [0,0,9,0,4,0,0,0,0]
p6 = [0,0,0,7,5,0,0,0,0]
p7 = [0,0,2,0,7,0,0,0,4]
p8 = [0,0,0,0,0,3,6,1,0]
p9 = [0,0,0,0,0,0,8,0,0]
pf = [p1,p2,p3,p4,p5,p6,p7,p8,p9]
start_time = time.time()

def sodokusolver (p) :
    print ("New puzzle, non-zero count",np.count_nonzero(p))
    pizza = np.array(p)
    print(pizza)

    bestGrade = 81
    random.seed(time.time())
    attempts = 8000
    for i in range (attempts) : # number of attempts to solve
        if 0 == i % 1000 :
            print("."),
        random.seed(i)
        puzzlecopy = copy.deepcopy(p)
        puzzlecopy = solve(puzzlecopy, 0)
        myGrade = grade(puzzlecopy)
        if 0 ==myGrade :
            print("solved (tries)", i, "time elapsed", time.time() - start_time, "grade", myGrade, "nonzeros",np.count_nonzero(puzzlecopy))
            pizza = np.array(puzzlecopy)
            print(pizza)
            return i
        if myGrade < bestGrade  :
            bestGrade = min(myGrade, bestGrade)
            bestSolution = copy.deepcopy(puzzlecopy)
            #print("time elapsed", time.time()-start_time,"grade", myGrade, puzzlecopy)
    print("Can't solve attempts", attempts, "myBestGrade", bestGrade)
    pizza = np.array(bestSolution)
    print(pizza)
    return -999

sodokusolver(pa)
sodokusolver(pb)
sodokusolver(pc)
sodokusolver(pd)
sodokusolver(pe)
sodokusolver(pf)

# returns a valid sodoku puzzle of random number of entries from 1 to 80
def sodokurandom(initpuzzle) :
    m = copy.deepcopy(initpuzzle)
    #entrytarget = random.randint(40)
    #print entrytarget
    for i in range (40,60) :
        x = random.randint(0,8)
        y = random.randint(0,8)
        z = random.randint(1,9)
        #print x,y,z
        if 1 == isValid(m, [x,y,z]):
            m[x][y] = z
    return (m)

jmax = 0
jmaxproblem = copy.deepcopy(pc)
for i in range (40) :
    pz = sodokurandom(pc)
    j = sodokusolver(pz)
    if jmax < j :
        jmax = j
        jmaxproblem = copy.deepcopy(pz)
print("most difficult random problem", jmax, jmaxproblem)






