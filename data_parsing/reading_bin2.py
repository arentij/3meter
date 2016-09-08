import struct

with open('../data/032516/binlog/032516_3.bin', mode='rb') as inf:
    i = 0
    for line in inf:
        print(line)

        # print(struct.unpack('f', line))

        i += 1
        if i >= 16:
            break

