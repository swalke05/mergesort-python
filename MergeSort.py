import fileinput

#might be able to get rid of n with python
def TopDownMergeSort(A, B, n):
    TopDownSplitMerge(A, 0, n, B)

def TopDownSplitMerge(A, iBegin, iEnd, B):
    print "iBegin: ",iBegin
    print "iEnd: ",iEnd
    if (iEnd - iBegin < 2):
        return


    iMiddle = (iEnd + iBegin) / 2                   #Middle index of the array

    print "calling split left"
    print "a: " , A
    print "b: " , B
    TopDownSplitMerge(A, iBegin, iMiddle, B)        #Split / merge left half

    print "calling split right"
    print "a: " , A
    print "b: " , B
    TopDownSplitMerge(A, iMiddle, iEnd, B)          #Split / merge right half

    print "calling merge 2 halves"
    print "a: " , A
    print "b: " , B
    TopDownMerge(A, iBegin, iMiddle, iEnd, B)       #Merge the two halves

    print "calling copy"
    print "a: " , A
    print "b: " , B
    CopyArray(B, iBegin, iEnd, A)                   #copy merged sub-arrays back to A

def TopDownMerge(A, iBegin, iMiddle, iEnd, B):
    i = iBegin
    j = iMiddle
    print ("in TopDownMerge")
    print "iBegin: ", iBegin
    print "iMiddle: ", iMiddle
    print "iEnd", iEnd
    #While there are elements in the left or right runs
    #different in python
    for k in range(iBegin, iEnd):
        #If left sub-array head exists and is <= existing right sub-array head
        print k
        if (i < iMiddle and (j >= iEnd or A[i] <= A[j])):
            B[k] = A[i]
            i+=1
        else:
            B[k] = A[j]
            j+=1

def initializeB(A, B):
    for num in A:
        B.append(0)

def CopyArray(B, iBegin, iEnd, A):
    for k in range(iBegin, iEnd):
        A[k] = B[k]

if __name__ == "__main__":
    fileContents = ""
    A = []
    B = []

    for line in fileinput.input(None):
        fileContents = fileContents + line

    A = map(int, fileContents.split(' '))

    initializeB(A, B)
    #print (A)
    #print (B)

    TopDownMergeSort(A, B, len(A) )
    print(A)