with open('../data/032516/training.txt', mode='r') as inf:
    raw_data = []
    file_len = 0
    # creating raw data
    for line in inf:
        file_len += 1
        raw_data.append(float(line))

f = 256
dt = 30
ch = 47

# number of turns of 30s with 256 times per second
n = file_len/f/dt/(ch+1)

# list of times
t = []
# list of data
data = [[] for i in range(ch)]

# print(len(raw_data))
# print(file_len)

# checking if there are really time + 47 channels
if n % 1 != 0:
    raise NameError('not 48 channels')
else:
    n = int(n)


for i_n in range(n):
    for i_t in range(dt*f):

        t.append(raw_data[i_t + i_n * f * dt * (ch+1)])
    for i_ch in range(ch):
        for i_t in range(dt*f):

            data[i_ch].append(raw_data[i_t + (1+i_ch) * f * dt + i_n * (ch+1) * f * dt])


for k in range(0, len(t), 256):
    print(t[k], ' ', end='')
    for i_ch in range(ch):
        print(data[i_ch][k], end=' ')
    print()
