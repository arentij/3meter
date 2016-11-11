import scipy.io as sio

data = sio.loadmat('../data/2516/032516.mat')

i = 0
# for ob in data:
#     print(ob)
#     i += 1
#     if i == 100:
#         break
print(data)
