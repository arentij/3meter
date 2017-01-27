import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np

name = lambda x: [n for n in globals() if id(globals()[n])==id(x)][0]


def checking_sigma(f):

    key = name(f)
    print(key)

    n = len(f[key])
    print(n)

    average_step = (f[key][-1][0] - f[key][0][0])/n

    khi = 0
    for i in range(n-1):
        khi += (f[key][i+1][0] - f[key][i][0] - average_step)**2

    print(average_step, 1/256)
    print((khi/(n+1))**0.5)


def loading_mat():
    # p05 = sio.loadmat('../data/pressure4SSR/p05.mat')
    # p1 = sio.loadmat('../data/pressure4SSR/p1.mat')
    # p15 = sio.loadmat('../data/pressure4SSR/p15.mat')
    # p2 = sio.loadmat('../data/pressure4SSR/p2.mat')
    # p25 = sio.loadmat('../data/pressure4SSR/p25.mat')
    # p3 = sio.loadmat('../data/pressure4SSR/p3.mat')
    p35 = sio.loadmat('../data/pressure4SSR/p35.mat')
    return p35



tp = dict()
tp['p05'] = [61245, 61910, 62500, 63100, 63700, 64200, 64700, 65300]
tp['p1'] =  [51000, 51390, 51904, 52400, 52900, 53420, 53900, 54400]
tp['p15'] = [55602, 56200, 56800, 57400, 58000, 58600, 59200, 59800]
tp['p2'] =  [53400, 53800, 54200, 54600, 55020, 55400, 55800, 56200]
tp['p25'] = [59300, 59500, 59800, 60100, 60400, 60700, 61000, 61300]
tp['p3'] =  [58600, 58900, 59200, 59500, 59800, 60200, 60502, 60800]
tp['p35'] = [65200, 65400, 65650, 65800, 66000, 66200, 66400, 66600]

step = 1/256


gap = 5


def creating_pressure(f):
    key = name(f)
    n = len(f[key])
    p = [[], [], [], [], [], [], []]

    for i in range(n):
        t = f[key][i][0]
        # print(t)
        k = -1
        for j in range(7):

            if tp[key][j] <= t <= tp[key][j+1]:
                if tp[key][j]/2 + tp[key][j+1]/2 < t < tp[key][j+1] - gap:
                    k = j
                    break
                else:
                    break

        if k != -1:
            p[k].append(f[key][i][1])

    # for i in range(n):
    #     if f[key][i]==0:
    #         break

    # returning a list with pressure data, so creating_pressure[0] - will give a list with data
    # of pressure for first time period from tp(f)
    return p

p35 = loading_mat()

p = creating_pressure(p35)

s0 = p[0]
s20 = p[1]
s40 = p[2]
s80 = p[3]
s160 = p[4]
s270 = p[5]
s02 = p[6]

# checking_sigma(p1)


dt = 1/256
Fs = 1/dt
# t = np.arange(0, len(p)/256, dt)
# nse = np.random.randn(len(t))
# r = np.exp(-t/0.05)

# cnse = np.convolve(nse, r)*dt
# cnse = cnse[:len(t)]
# s = p

# plt.subplot(3, 2, 1)
# plt.plot(t, s)

# plt.subplot(3, 2, 3)
# plt.magnitude_spectrum(s, Fs=Fs)

x_lim = [0, 7]
y_lim = [3, 60]
'''
plt.subplot(111)
plt.magnitude_spectrum(s0, Fs=Fs, scale='dB')
plt.title('Rate=2,        B = 0')
plt.xlim(x_lim)
plt.ylim(y_lim)
plt.savefig('r2b0.png')
#
plt.subplot(111)
plt.magnitude_spectrum(s80, Fs=Fs, scale='dB')
plt.title('Rate=2,        B = 80')
plt.xlim(x_lim)
plt.ylim(y_lim)
plt.savefig('r2b80.png')

#
plt.subplot(111)
plt.magnitude_spectrum(s270, Fs=Fs, scale='dB')
plt.title('Rate=2,        B = 270')
plt.xlim(x_lim)
plt.ylim(y_lim)
plt.savefig('r2b270.png')
'''

for i2 in range(7):
    plt.plot(11)
    plt.magnitude_spectrum(p[i2], Fs=Fs, scale='dB')

    if i2 == 7 or i2 == 0:
        B = 0
    elif i2 == 6:
        B = 270
    else:
        B = 10*2**i2


    plt.title('Rate = 35,  B = ' + str(B))
    plt.xlim(x_lim)
    plt.ylim(y_lim)
    plt.show()
    input()
    # plt.savefig('r05' + str(i2) + '.png')
    plt.close()

#
# plt.subplot(3, 2, 5)
# plt.angle_spectrum(s, Fs=Fs)
#
# plt.subplot(3, 2, 6)
# plt.phase_spectrum(s, Fs=Fs)

plt.show()
