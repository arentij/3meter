def read_abstime(f):
    with open(f, mode='rb') as inf_abst:
        data_abst = inf_abst.read()
        for i in data_abst.split():
            print(float(i))


def read_data(f):
    with open(f, mode='rb') as inf:
        return inf.read()
        # n = len(data)
        # print(n/256./30.)


# read_abstime('../data/032516/binlog/032516_3_abstime')

print()

data = read_data('../data/032516/binlog/032516_3.bin')

str_data = {'t':[]}
for i in range(1, 48):
    str_data[i] = []

# print(str_data)

n = len(data)
# print(n/30/256/48.)

index = 0
for i in range(int(n/30/256/48)):
    for j in range(256*30):
        str_data['t'].append(data[index])
        index += 1
    for m in range(1, 48):
        for j in range(256*30):
            str_data[m].append(data[index])
            index += 1

print("here we go")
print(str_data['t'])

