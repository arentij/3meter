# import random
dt = 30  # interval in seconds of recording
f = 256  # frequency of recordings
n = 47  # number of channels
m = 2   # number of times if writing dt*f*n
start = 0
t = [start + i/f for i in range(dt*f*m)]

# next sting creates data with 
data = [[(j+1)*100+t[i] for i in range(dt*f*m)] for j in range(n)]

# print(*t, sep=' ')
# print()
# for i in range(n):
#     print(*data[i])
#     print()

with open('../data/032516/training.txt', mode='w') as ouf:

    for im in range(m):
        for it in range(dt*f):
            # print(t[dt*f*im + it])
            ouf.write(str(t[dt*f*im + it])+'\n')
        # print('EOT--------')
        for ch in range(n):
            for it in range(dt*f):
                # print(data[ch][it])
                ouf.write(str(data[ch][it])+'\n')

            # print('EOCH---------', ch)
        # print('EOI--------', im)
