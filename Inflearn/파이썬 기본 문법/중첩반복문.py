'''
중첩 반복문 (2중 for문)
'''

'''
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
'''
for i in range(5):
    for j in range(5):
        print(j, end=' ')
    print()

'''
*
**
***
****
*****
'''
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

'''
*****
****
***
**
*
'''
for i in range(5):
    for j in range(5-i):
        print('*', end='')

    print()