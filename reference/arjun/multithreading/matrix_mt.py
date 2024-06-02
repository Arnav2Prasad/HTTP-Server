#!/usr/bin/python

# multithreaded code for addition of two square matrices
# output matirix is printed
# each row is added on a different thread of execution

from threading import Thread

# adds the kth row of a j x j order matrix
def add(k, j, mat1, mat2, mat3):
    for i in range(j):
        mat3[k][i] = mat1[k][i] + mat2[k][i]

# main function that does the matrix addition
def Main():
    # order of the square matrix
    matorder = 100;

    # define 2D arrays for each matrix
    mat1 = [[0]*matorder]*matorder
    mat2 = [[0]*matorder]*matorder
    mat3 = [[0]*matorder]*matorder

    # take input for mat1
    for m in range(matorder):
        for n in range(matorder):
            mat1[m][n] = int(input())

    # take input for mat2
    for m in range(matorder):
        for n in range(matorder):
            mat2[m][n] = int(input())

    # empty array for storing the threads
    t = [];

    # create a thread for adding each row of mat1 and mat2
    # start the execution for the thread
    # store the thread in the array of threads
    for i in range(matorder):
        th = Thread(target = add, args = (i, matorder, mat1, mat2, mat3))
        th.start()
        t.append(th)

    # now join all the threads
    # here, completed thread will have to wait until all have been joined
    for i in range(matorder):
        t[i].join()

    # display mat3 as output
    print("mat3")
    for m in range(matorder):
        for n in range(matorder):
            print(mat3[m][n], end = ' ')
    
    # newline :)
    print()

if __name__ == "__main__":
    Main()
