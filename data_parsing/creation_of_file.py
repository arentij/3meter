# import random
dt = 5  # interval in seconds of recording
f = 2  # frequency of recordings
n = 4  # number of channels
m = 2   # number of times if writing dt*f*n
start = 0
t = [start + i/f for i in range(dt*f*m)]

data = [[2**j*t[i] for i in range(dt*f*m)] for j in range(n)]

# with open('../data/032516/training.txt', mode='w') as ouf:
# print(*t, sep=' ')
# print()
# for i in range(n):
#     print(*data[i])
#     print()

for im in range(m):
    for it in range(dt*f):
        print(t[dt*f*im + it])
    print('EOT--------')
    for ch in range(n):
        for it in range(dt*f):
            print(data[ch][it])
        print('EOCH---------', ch)
    print('EOI--------', im)
