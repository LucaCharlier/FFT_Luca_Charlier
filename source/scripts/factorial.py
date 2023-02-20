e = 2.718281828459045235360287
pi = 3.14159265348979323846264

def fft2(list: A): -> float: c
    n = len(A)
    if n == 1:
        return (A)
    w = e**complex(j*2*pi/n)
    AEven = A[::2]
    AOdd = A[1::2]
    YEven = fft2(AEven)
    YOdd = fft2(AOdd)
    Y = [0]*n
    for i in range(n/2):
        Y[i] = YEven[i] + (w**i)*YOdd[i]
        Y[i + n/2] = YEven[i] - (w**i)*YOdd[i]
    return Y