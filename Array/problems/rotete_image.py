# https://app.codesignal.com/interview-practice/topics/arrays

def rotateImage(a):
    rotate =  [[ None for i in range(0, len(a)) ] for j in range(0, len(a)) ]
    for i in range(0, len(a)):
        for j in range(0, len(a[i])):
            if not rotate[j][len(a)-1-i]:
                rotate[j][len(a)-1-i] = a[i][j]
    return rotate