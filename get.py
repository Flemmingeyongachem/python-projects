n=int(input('enter the number: '))
def sumToN(m):
    for i in range(1, m+1):
        summer = 0
        for j in range(1, i+1):
            if j == 1:
                summer = summer + 1
                print(1, end='')
            else:
                print(f' + {j}', end='')
                summer = summer + j
        print(f' = {summer}')
sumToN(n)